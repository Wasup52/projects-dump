<html>
    <head>
        <script
            src="https://code.jquery.com/jquery-3.2.1.min.js"
            integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
            crossorigin="anonymous"
        ></script>
        <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
        <!-- <script src="mousetrap.min.js" charset="utf-8"></script> -->

        <link rel="icon" href="/img/TwitchRat.png" type="image/x-icon" />

        <!-- <link rel="stylesheet" href="/css/bootstrap.min.css" />
        <link rel="stylesheet" href="/css/all.min.css" />
        <link rel="stylesheet" href="/css/mdb.min.css" /> -->

        <link href="https://vjs.zencdn.net/7.2.3/video-js.css" rel="stylesheet">

        <link rel="stylesheet" href="/css/player.css">

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
                <video id='video' class="video-js vjs-default-skin vjs-fluid vjs-big-play-centered" width="100%" controls>
                    <source id="video-src" type="application/x-mpegURL" scr="">
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
    </body>
    <script src="/js/mousetrap.min.js" charset="utf-8"></script>
    <script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>

    <script src="/js/Utils.js"></script>
    <script src="/js/ChatGetter.js"></script>
    <script src="chat-parser-mobile.js"></script>
    <script src="player-mobile.js"></script>
</html>
