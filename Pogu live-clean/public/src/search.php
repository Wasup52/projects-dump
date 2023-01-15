<?php

function dump($var) {
    echo '<pre>';
    var_dump($var);
    echo '</pre>';
}

function getSearch($querry) {
    $url = "https://twitchtracker.com/search?q=" . $querry;
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
    $response = curl_exec($ch);
    curl_close($ch);

    echo $response;

    $pattern = '/<div class="col-xs-12 col-sm-6">.*<\/div>/';
    preg_match_all($pattern, $response, $matches);
    dump($matches);
    return $matches[0];
}

echo getSearch("aminematue");

?>