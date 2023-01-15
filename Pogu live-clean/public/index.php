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

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">

    <link rel="stylesheet" href="/css/index.css">

</head>

<body class="dark-theme" style="height: 100%">
    <header>
        <?php include "elements/navbar.php" ?>
    </header>
    <h1 style="font-size: var(--font-size-1);">Home</h1>
</body>

</html>

