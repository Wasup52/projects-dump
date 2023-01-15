<?php

require_once "getVod.php";

function createVideoCard($href, $title, $thumbnail) {

    return <<<HTML
    <div class="col">
        <a href="$href">
            <div class="card shadow-sm">
                <img class="bd-placeholder-img card-img-top" width="100%" height="225" src="$thumbnail">

                <div class="card-body">
                    <div class="row">
                        <div class="col">
                            $title
                        </div>
                        <div class="col-auto">
                            <img src="https://static-cdn.jtvnw.net/ttv-boxart/509658-54x72.jpg" title="" data-original-title="Just Chatting">
                            <img src="https://static-cdn.jtvnw.net/ttv-boxart/518006_IGDB-54x72.jpg" title="" data-original-title="Stray">
                            <img src="https://static-cdn.jtvnw.net/ttv-boxart/509658-54x72.jpg" title="" data-original-title="Just Chatting">
                        </div>
                    </div>
                    <!-- <div class="bg-light d-flex justify-content-between">
                        <div></div>
                        <div>
                            <img src="https://static-cdn.jtvnw.net/ttv-boxart/509658-54x72.jpg" title="" data-original-title="Just Chatting">
                            <img src="https://static-cdn.jtvnw.net/ttv-boxart/518006_IGDB-54x72.jpg" title="" data-original-title="Stray">
                        </div>
                    </div> -->
                </div>
            </div>
        </a>
    </div>
    HTML;
}

if (isset($_GET["streamer"])) {
    $streamerName = $_GET["streamer"];
    $infos = getInfos($streamerName);

    $output = [];
    if ($infos["ok"]) {
        $hrefList = $infos[0];
        $titleList = $infos[1];
        $startTimeList = $infos[2];
        
        for ($i = 0; $i < count($hrefList); $i++) {
            $vodLink = getVod("https://twitchtracker.com" . $hrefList[$i], $startTimeList[$i]);
            $output = [
                "ok" => true,
                "vodLink" => $vodLink,
                "title" => $titleList[$i],
                "thumbnail" => getThumbnail($vodLink)
            ];
        }
    } else {
        $output = [
            "ok" => false,
            "error" => $infos["error"]
        ];
    }

}

?>

<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.101.0">
    <title>Album example · Bootstrap v5.2</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.2/examples/album/">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">

    <!-- Favicons -->
    <link rel="icon" href="/img/TwitchRat.png" type="image/x-icon" />
    <meta name="theme-color" content="#712cf9">


    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }

        .b-example-divider {
            height: 3rem;
            background-color: rgba(0, 0, 0, .1);
            border: solid rgba(0, 0, 0, .15);
            border-width: 1px 0;
            box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
        }

        .b-example-vr {
            flex-shrink: 0;
            width: 1.5rem;
            height: 100vh;
        }

        .bi {
            vertical-align: -.125em;
            fill: currentColor;
        }

        .nav-scroller {
            position: relative;
            z-index: 2;
            height: 2.75rem;
            overflow-y: hidden;
        }

        .nav-scroller .nav {
            display: flex;
            flex-wrap: nowrap;
            padding-bottom: 1rem;
            margin-top: -1px;
            overflow-x: auto;
            text-align: center;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
        }
    </style>


</head>

<body>
    <header>
        <div class="navbar navbar-dark bg-dark shadow-sm">
            <div class="container">
                <a href="#" class="navbar-brand d-flex align-items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor"
                        stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="me-2"
                        viewBox="0 0 24 24">
                        <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
                        <circle cx="12" cy="13" r="4" />
                    </svg>
                    <strong>Album</strong>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader"
                    aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </div>
    </header>

    <main>

        <section class="py-5 text-center container">
            <div class="row py-lg-5">
                <div class="col-lg-6 col-md-8 mx-auto">
                    <form action="/">
                        <div class="row">
                            <div class="col-8">
                                <input class="form-control" id="streamerName" placeholder="Streamer Name" name="streamer">
                            </div>
                            <div class="col-2">
                                <button type="submit" class="btn btn-primary">Search</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </section>

        <div class="album py-5 bg-light">
            <div class="container">

                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
                    <?php
                        if (!empty($output)) {
                            if ($output["ok"]) {
                                foreach ($output as $key => $infos) {
                                    echo createVideoCard("/player/#" . $infos['vodLink'], $infos['title'], $infos['thumbnail']);
                                }
                            } else {
                                echo '<h6>'.$output["error"].'</h6>';
                            }
                        }
                    ?>
                </div>
            </div>
        </div>
    </main>
</body>


</html>