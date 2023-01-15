<?php

if (isset($_GET["streamer"])) {
    $streamerName = $_GET["streamer"];
    
    header("Location: sub-only-vods.php?streamer=$streamerName"); //send to "sub-only-vods.php"
}

?>

<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Wasup">
    <title>Ratwitch</title>

    <link rel="icon" href="/img/TwitchRat.png" type="image/x-icon" />

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">

    <link rel="stylesheet" href="/css/index.css">

    <link href="/css/mbbootstrap.css" rel="stylesheet" />
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" rel="stylesheet" />

</head>

<body class="dark-theme" style="height: 100%">
    <header>

        <?php include "elements/navbar.php" ?>
    </header>
    <h1 style="font-size: var(--font-size-1);">Deleted Vods</h1>
    <div class="container" style="display: flex; justify-content: center !important;">
    
        <form class="px-1" id='form' style="width: 26rem;" action="" method="post">
            <!-- TwitchTracker link input -->
            <div class="form-outline mb-4">
                <input type="text" id="proxy-username" name="proxy-username" class="form-control" style="color: #fff;">
                <label class="form-label" for="proxy-username" style="margin-left: 0px; color: #fff;">Username</label>
                <div class="form-notch">
                    <div class="form-notch-leading" style="width: 9px;"></div>
                    <div class="form-notch-middle" style="width: 88.8px;"></div>
                    <div class="form-notch-trailing"></div>
                </div>
            </div>

            <button class='btn btn-primary btn-block mb-3 justify-content-center' id='fetch' style="background-color: #07b1e7;">
                <!-- #40bbde -->
                Fetch &nbsp;
                <i class="fas fa-cloud-download-alt"></i>
            </button>

        </form>
    </div>
</body>

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.3.0/mdb.min.js"></script>

</html>