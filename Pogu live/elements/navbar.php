<?php
require_once "Utils.php";
?>

<nav class="navbar navbar-expand navbar-dark" style="background-color: #292b45; font-size: var(--font-size-5)">
    <div class="container-fluid">
        <a href="/">
            <div class="navbar-brand py-0 ps-1" href="#">
                <img src="/img/TwitchRat.png" class="d-inline-block align-top" alt="Bootstrap" loading="lazy" width="32"
                    height="32">
            </div>
        </a>

        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <a href="/" style="text-decoration: none; color: #fff;">
                <li class="nav-item mt-2">
                    <h4 aria-current="page" style="font-size: var(--font-size-3_5)"><b>Ratwitch</b></h4>
                </li>
            </a>
            <li class="nav-item mt-1">
                <a class="nav-link"></a>
            </li>
            <li class="nav-item mt-1">
            <?= ($_SERVER["REQUEST_URI"] == "/sub-only-vods.php") ? navLink("Sub Only Vods", "/sub-only-vods.php", true) : navLink("Sub Only Vods", "/sub-only-vods.php", false) ?>
            </li>
            <li class="nav-item mt-1">
                <?= ($_SERVER["REQUEST_URI"] == "/deleted-vods.php") ? navLink("Deleted Vods", "/deleted-vods.php", true) : navLink("Deleted Vods", "/deleted-vods.php", false) ?>
            </li>
        </ul>

        <form class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3" role="submit">
            <div class="row justify-content-center">
                <div class="col-8">
                    <input type="search" class="form-control form-control-dark text-bg-dark" name="streamer" placeholder="Streamer Name" style="font-size: var(--font-size-5)">
                </div>
                <div class="col-2">
                    <button class="btn btn-outline-light" id="export" type="submit" style="font-size: var(--font-size-5)">Search</button>
                </div>
            </div>
        </form>
    </div>
</nav>