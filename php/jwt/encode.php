<?php
require('vendor/autoload.php');

use \Firebase\JWT\JWT;

$key = 'i_am_a_secret_key';

$json = json_decode(file_get_contents('php://stdin'));

if ($json === NULL){
    die("[Error] Invalid input.\n" . 'example: $ echo \'{"key1":"value1","expire":12345}\' | php encode.php' . "\n");
}

$jwt = JWT::encode($json, $key);

echo $jwt;
