<?php

// enable error reporting for debugging
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

function dump($var) {
    echo '<pre>';
    var_dump($var);
    echo '</pre>';
}

function getDomains($filePath) {
    $fileContent = file_get_contents($filePath);
    $domains = explode("\n", $fileContent);
    return $domains;
}

// get time diference from epoche
function getTimeDiff($time) {
    $time = new DateTime($time);
    $epoche = new DateTime("1970-01-01");

    $interval = $epoche->diff($time);
    $diff = $interval->days * 24 * 60 * 60 + $interval->h * 60 * 60 + $interval->i * 60 + $interval->s;

    return $diff;
}

function getVod($twitchTrackerUrl, $vodStartTime) {
    $streamerName = explode("/", $twitchTrackerUrl)[3];
    $vodID = explode("/", $twitchTrackerUrl)[5];

    $timeStamp = getTimeDiff($vodStartTime);
    $formatedString = $streamerName . "_" . $vodID . "_" . $timeStamp;

    // get sha1 hash of formatedString encode in utf8
    $hash = sha1(utf8_encode($formatedString));
    $requiredHash = substr($hash, 0, 20);

    $finalFormatedString = $requiredHash . "_" . $formatedString;

    $domains = getDomains("data/domains.txt");
    foreach ($domains as $domain) {
        $url = trim($domain) . "/" . $finalFormatedString . "/chunked/index-dvr.m3u8";

        // check if the content of the web page at url contains "#EXTM3U"
        try {
            $fileContent = file_get_contents($url);

            if (strpos($fileContent, "#EXTM3U") !== false) {
                return $url;
            } else {
                continue;
            }

        } catch (\Throwable $th) {
            continue;
        }
    }
}

function getThumbnail($vodLink) {
    $domainId = explode(".", explode("/", $vodLink)[2])[0];
    $idLink = explode("/", $vodLink)[3];
    $thumbnail = "https://static-cdn.jtvnw.net/cf_vods/" . $domainId . "/" . $idLink . "//thumb/thumb0-320x180.jpg";

    return $thumbnail;
}

function getInfos($streamerName) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, "https://twitchtracker.com/" . $streamerName);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $response = curl_exec($ch);
    curl_close($ch);

    $pattern = '/<a class="entity entity-line" href="(.*)" title="(.*)" data-toggle="tooltip">\n<div data-dt="(.*)">/';
    
    preg_match_all($pattern, $response, $matches);

    $hrefList = $matches[1];
    $titleList = $matches[2];
    $startTimeList = $matches[3];

    if (empty($hrefList)) {
        $pattern = '/Checking if the site connection is secure/';
        preg_match_all($pattern, $response, $matches);

        if (empty($matches)) {
            $error = "Streamer not found";
        } else {
            $error = "Request blocked by Cloudflare";
        }

        $return = [
            "ok" => false,
            "infos" => [$hrefList, $titleList, $startTimeList],
            "error" => $error
        ];
    } else {
        $return = [
            "ok" => true,
            "infos" => [$hrefList, $titleList, $startTimeList],
            "error" => ""
        ];
    }

    return $return;
}

function delay($seconds) {
    $delay = $seconds * 1000000;
    usleep($delay);
}

function getInfosFromTwitch($streamerName) {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, "https://gql.twitch.tv/gql");
    curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        'Client-Id: kimne78kx3ncx6brgo4mv6wki5h1ko',
    ));
    $post_data = [
        [
            "operationName" => "FilterableVideoTower_Videos",
            "variables" => [
                "limit" => 30,
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
    dump($payload);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

    $response = curl_exec($ch);
    curl_close($ch);

    $data = json_decode($response, true);

    dump($data);

    
}

$infos = getInfosFromTwitch("aminematue");
// $infos = getInfos("aminematue");
// $hrefList = $infos[0];
// $titleList = $infos[1];
// $startTimeList = $infos[2];

// dump($infos);

// $output = [];
// for ($i = 0; $i < count($hrefList); $i++) {
//     $vodLink = getVod("https://twitchtracker.com" . $hrefList[$i], $startTimeList[$i]);
//     $output[] = [
//         "vodLink" => $vodLink,
//         "title" => $titleList[$i],
//         "thumbnail" => getThumbnail($vodLink)
//     ];
// }

// dump($output);


?>