<?php
require_once "Utils.php";

class ChatGetter {
    private $twitchApiUrl = "https://gql.twitch.tv/gql";
    private $twitchApiHeaders = [
        'Client-Id: kimne78kx3ncx6brgo4mv6wki5h1ko', // this is the client id of the twitch web app
    ];
    private $numberOfVodsLimit = 30;

    public function getChat($vodId) {
        $firstData = [
            [
                    "operationName" => "VideoCommentsByOffsetOrCursor",
                    "variables" => [
                        "videoID" => "1601548777",
                        "contentOffsetSeconds" => 30
                    ],
                    "extensions" => [
                        "persistedQuery" => [
                            "version" => 1,
                            "sha256Hash" => "b70a3591ff0f4e0313d126c6a1502d79a1c02baebb288227c582044aa76adf6a"
                    ]
                ]
            ]
        ];

        $lastCommentCursor = $this->getLatestCommentCursor($vodId);

        $folowingData = [
            [
                "operationName" => "VideoCommentsByOffsetOrCursor",
                "variables" => [
                    "videoID" => "1601548777",
                    "cursor" => $lastCommentCursor,
                ],
                "extensions" => [
                    "persistedQuery" => [
                        "version" => 1,
                        "sha256Hash" => "b70a3591ff0f4e0313d126c6a1502d79a1c02baebb288227c582044aa76adf6a"
                    ]
                ]
            ]
        ];
                    
        // ...
    }

    // ----------------- DATA RETRIEVAL -----------------


    // ----------------- DATA PARSING FUNCTIONS ----------------- 


    // ----------------- FILE HANDLING -----------------

}

?>