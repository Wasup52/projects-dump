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

    <?php
        if (isset($src)) {
            echo <<<HTML
            <video id='vod' class="video-js vjs-default-skin vjs-fluid vjs-big-play-centered" width="100%" controls>
                <source type="application/x-mpegURL" src="$src">
            </video>
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
    
    <!-- <video id='vod' class="video-js vjs-default-skin vjs-fluid vjs-big-play-centered" width="100%" controls>
        <?= isset($src) ? '<source type="application/x-mpegURL" src="' . $src . '">' : "<h6>Vod Not Found<h6>" ?>
    </video> -->

</html>


<!-- JS code -->
<script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
<!-- If you'd like to support IE8 (for Video.js versions prior to v7) -->
<!-- <script src="https://vjs.zencdn.net/ie8/ie8-version/videojs-ie8.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/videojs-contrib-hls/5.14.1/videojs-contrib-hls.js"></script>
<script src="https://vjs.zencdn.net/7.2.3/video.js"></script> -->

<script>
    var playerJS = videojs('vod', {
        playbackRates: [0.5, 1, 1.5, 2]
    });

    playerJS.fill(true);
    playerJS.play();
</script>