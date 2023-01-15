<?php
require_once "Utils.php";

class VodGetter {
    private $twitchApiUrl = "https://gql.twitch.tv/gql";
    private $twitchApiHeaders = [
        'Client-Id: kimne78kx3ncx6brgo4mv6wki5h1ko',
    ];
    private $numberOfVodsLimit = 30;

    public static function formatLength($timeInSec) {
        $hours = floor($timeInSec / 3600);
        $minutes = floor(($timeInSec / 60) % 60);
        $seconds = $timeInSec % 60;

        return sprintf("%02d:%02d:%02d", $hours, $minutes, $seconds);
    }

    public static function getPassedTime($publishedAt) {
        $publishedAt = new DateTime($publishedAt);
        $now = new DateTime();
        $interval = $now->diff($publishedAt);

        // add years, days,hours, etc. to get the time in sec
        $passedTime = $interval->y * 31536000 + $interval->d * 86400 + $interval->h * 3600 + $interval->i * 60 + $interval->s;

        return $passedTime;
    }

    public static function formatPassedTime($timeInSec) { // if time is greater than a days return n days ago, if greater than a month return n months ago, if greater than a year return n years ago, else return n hours ago
        $hours = floor($timeInSec / 3600);
        $days = floor($timeInSec / 86400);
        $months = floor($timeInSec / 2592000);
        $years = floor($timeInSec / 31536000);

        if ($years > 0) {
            if ($years == 1) {
                return "Last year";
            } else {
                return "$years years ago";
            }
        } else if ($months > 0) {
            if ($months == 1) {
                return "Last month";
            } else {
                return "$months months ago";
            }
        } else if ($days > 0) {
            if ($days == 1) {
                return "Yesterday";
            } else {
                return "$days days ago";
            }
        } else {
            if ($hours == 1) {
                return "1 hour ago";
            } else {
                return "$hours hours ago";
            }
        }
    }

    public static function formatStartTime($startTime) { // the format if dd Mon, yyyy
        $startTime = new DateTime($startTime);
        $startTime = $startTime->format("d M, Y");

        return $startTime;
    }

    /**
     * get the vods either from the twitch or from the cache
     * 
     * @param string $streamerName
     * @return array
     */
    public function getVods($streamerName) {
        if ($this->isAlreadySaved($streamerName)) {
            if ($this->dataIsUpToDate($streamerName)) { // check if data is less than 1 hour old
                $data = $this->getDataFromFile($streamerName);
                echo "Data gotten from file";
            } else {
                $data = $this->getDataFromTwitch($streamerName);
                $this->saveDataToFile($streamerName, $data); // update data
                echo "Data gotten from Twitch and updated saved data";
            }
        } else {
            $data = $this->getDataFromTwitch($streamerName);
            $this->saveDataToFile($streamerName, $data); // save data to prevent multiple requests
            echo "Data gotten from Twitch and saved";
        }

        $output = [];
        for ($i = 0; $i < $this->getNumberOfVods($data); $i++) {
            $output[$i]["title"] = $this->getVodTitle($data, $i);
            $output[$i]["thumbnail"] = $this->getThumbnailUrl($data, $i);
            $output[$i]["animatedPreview"] = $this->getAnimatedPreviewUrl($data, $i);
            $output[$i]["length"] = $this->getVodLength($data, $i);
            $output[$i]["publishedAt"] = $this->getVodStartTime($data, $i);
            $output[$i]["videoID"] = $this->getVideoID($data, $i);
            $output[$i]["vodUrl"] = $this->getVodUrl($data, $i);
        }

        $return = [
            "ok" => true,
            "data" => $output
        ];

        return $output;
    }

    // ----------------- DATA RETRIEVAL -----------------

    /**
     * get the data from the saved file
     * 
     * @param string $streamerName
     * @return array
     */
    private function getDataFromFile($streamerName) {
        $file = fopen("data/vods/$streamerName.json", "r");
        $savedData = fread($file, filesize("data/vods/$streamerName.json"));
        fclose($file);

        $savedData = json_decode($savedData, true);

        return $savedData["data"];
    }

    /**
     * get the data from the twitch server
     * 
     * @param string $streamerName
     * @return array
     */
    private function getDataFromTwitch($streamerName) {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $this->twitchApiUrl);
        curl_setopt($ch, CURLOPT_HTTPHEADER, $this->twitchApiHeaders);
        $post_data = [
            [
                "operationName" => "FilterableVideoTower_Videos",
                "variables" => [
                    "limit" => $this->numberOfVodsLimit,
                    "channelOwnerLogin" => $streamerName,
                    "broadcastType" => null,
                    "videoSort" => "TIME",
                ],
                "extensions" => [
                    "persistedQuery" => [
                        "version" => 1,
                        "sha256Hash" => "a937f1d22e269e39a03b509f65a7490f9fc247d7f83d6ac1421523e3b68042cb",
                    ]
                ],
            ],
        ];
        $payload = json_encode($post_data);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

        $response = curl_exec($ch);
        curl_close($ch);

        return json_decode($response, true);
    }

    // ----------------- DATA PARSING FUNCTIONS ----------------- 

    private function getNumberOfVods($data) {
        return sizeof($data[0]["data"]["user"]["videos"]["edges"]);
    }

    private function getAnimatedPreviewUrl($data, $index) {
        return $data[0]["data"]["user"]["videos"]["edges"][$index]["node"]["animatedPreviewURL"];
    }

    private function getThumbnailUrl($data, $index) {
        $thumbnailUrl = $data[0]["data"]["user"]["videos"]["edges"][$index]["node"]["previewThumbnailURL"];
        
        if ($thumbnailUrl == "https://vod-secure.twitch.tv/_404/404_processing_320x180.png") {
            $thumbnailUrl = "/img/thumb-placeholder-320x180.jpg";
        }

        return $thumbnailUrl;
    }

    private function getVodUrl($data, $index) {
        $videoId = $data[0]["data"]["user"]["videos"]["edges"][$index]["node"]["id"];
        $animatedThumbUrl = $this->getAnimatedPreviewUrl($data, $index);
        $vodUrl = str_replace("/storyboards/$videoId-strip-0.jpg", "/chunked/index-dvr.m3u8", $animatedThumbUrl);

        return $vodUrl;
    }

    private function getVodTitle($data, $index) {
        return $data[0]["data"]["user"]["videos"]["edges"][$index]["node"]["title"];
    }

    private function getVodLength($data, $index) {
        return $data[0]["data"]["user"]["videos"]["edges"][$index]["node"]["lengthSeconds"];
    }

    private function getVodStartTime($data, $index) {
        $publicheTime = $data[0]["data"]["user"]["videos"]["edges"][$index]["node"]["publishedAt"];
        $publicheTime = str_replace("T", " ", $publicheTime);
        $publicheTime = str_replace("Z", "", $publicheTime);

        return $publicheTime;
    }
    
    private function getVideoID($data, $index) {
        return $data[0]["data"]["user"]["videos"]["edges"][$index]["node"]["id"];
    }

    // ----------------- FILE HANDLING -----------------

    /**
     * save data to file
     * 
     * @param string $streamerName
     * @param array $data
     * @return void
     */
    private function saveDataToFile($streamerName, $data) {
        $file = fopen("data/vods/$streamerName.json", "w");
        $savedData = [
            "data" => $data,
            "timestamp" => time(),
        ];
        fwrite($file, json_encode($savedData));
        fclose($file);
    }

    /**
     * Check if data is already saved in a file
     * 
     * @param string $streamerName
     * @return bool
     */
    private function isAlreadySaved($streamerName) {
        return file_exists("data/vods/$streamerName.json");
    }

    /**
     * Check if data is less than 1 hour old
     * 
     * @param string $streamerName
     * @return bool
     */
    private function dataIsUpToDate($streamerName) {
        $file = fopen("data/vods/$streamerName.json", "r");
        $savedData = fread($file, filesize("data/vods/$streamerName.json"));
        fclose($file);

        $savedData = json_decode($savedData, true);
        
        return time() - $savedData["timestamp"] < 3600; // 1 hour = 3600 seconds
    }
}

// $vg = new VodGetter();
// $vods = $vg->getVods("maximebiaggi");
// dump($vods);
?>