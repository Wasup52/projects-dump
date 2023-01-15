<?php

function dump($var) {
    echo "<pre>";
    var_dump($var);
    echo "</pre>";
}

// dump($_POST["title"]);

?>

<html>
    <head>
        <link rel="icon" href="/img/TwitchRat.png" type="image/x-icon" />

        <!-- <link rel="stylesheet" href="/css/bootstrap.min.css" />
        <link rel="stylesheet" href="/css/all.min.css" />
        <link rel="stylesheet" href="/css/mdb.min.css" /> -->

        <link rel="stylesheet" href="/css/player.css">

        <style>
            #video {
                /* position: relative; */
                top: 0px;
                right: 0px;
                bottom: 0px;
                left: 0px;
                /* margin: auto; */

                height: 100%;
                width: 100%;

                max-height: 100%;
                max-width: 100%;

                background: black;
            }
        </style>

        <title>
            <?php 
                if (isset($_POST["title"])) {
                    echo $_POST["title"];
                } else {
                    echo "Vod Player";
                }
            ?>
        </title>
    </head>

    <body style="height: 100%; background: black;">
        <div class="row" style="height: 100%;">
            <div class="col">
                <video
                    id="video"
                    class="vod-player"
                    controls
                    autopictureinpicture
                ></video>
                <div class="video-upper-left-corner">
                    <div class="video-overlay"><i class="fas fa-angle-double-left"></i></span></div>
                </div>
            </div>
            <div class="col-auto" style="height: 100%;">
                <div class="chat-pannel-layout">
                    <div class="chat-pannel">
                        <div class="chat-header">
                            <span>Chat of Vod</span>
                        </div>
                        <div class="chat-container-layout">
                            <div id="chat-wrapper" class="chat-container-wrapper">
                                <div id="chat-container" class="chat-container">
                                    <ul id="chat-list-container" class="chat-list-container">
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
        </div>
    </body>

    <!-- <script
        src="https://code.jquery.com/jquery-3.2.1.min.js"
        integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
        crossorigin="anonymous"
    ></script> -->
    <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
    <script src="/js/mousetrap.min.js" charset="utf-8"></script>

    <script src="/js/Utils.js"></script>
    <script src="/js/ChatGetter.js"></script>
    <script src="chat-parser.js"></script>
    <script src="player.js"></script>
</html>
