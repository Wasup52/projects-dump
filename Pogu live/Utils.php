<?php

function dump($var) {
    echo '<pre>';
    var_dump($var);
    echo '</pre>';
}

function navLink($text, $link, $active)
{
    if ($active) {
        return "<a class='nav-link active fw-bold' href='$link'>$text</a></li>";
    } else {
        return "<a class='nav-link' href='$link'>$text</a>";
    }
}

?>