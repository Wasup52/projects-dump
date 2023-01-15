<?php

if (isset($_GET["src"])) {
    $src = $_GET["src"];
}

?>

<html>

    <head>

        <link rel="icon" href="/img/TwitchRat.png" type="image/x-icon" />

        <!-- CSS  -->
        <link href="https://vjs.zencdn.net/7.2.3/video-js.css" rel="stylesheet">
        
    </head>

    <body style="height: 100%; background: black;">
        <?php
            if (isset($src)) {
                echo <<<HTML
                <div class="row" style="height: 100%;">
                    <div class="col">
                        <video id='video' class="video-js vjs-default-skin vjs-fluid vjs-big-play-centered" width="100%" controls>
                            <source type="application/x-mpegURL" src="$src">
                        </video>
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
                HTML;
            } else {
                echo <<<HTML
                <div class="container">
                    <div class="row">
                        <div class="col">
                            <div class="card shadow-sm">
                                <div class="card-body">
                                    <div class="row">
                                        <div class="col">
                                            <h1>No vod to play</h1>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                HTML;
            }
            
        ?>
    </body>


</html>


<!-- JS code -->
<script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
<!-- If you'd like to support IE8 (for Video.js versions prior to v7) -->
<!-- <script src="https://vjs.zencdn.net/ie8/ie8-version/videojs-ie8.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/videojs-contrib-hls/5.14.1/videojs-contrib-hls.js"></script>
<script src="https://vjs.zencdn.net/7.2.3/video.js"></script> -->

<script src="/player-mobile/chat-parser-mobile.js"></script>