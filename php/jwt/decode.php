<?php
require('vendor/autoload.php');

use \Firebase\JWT\JWT;

$key = 'i_am_a_secret_key';

$jwt = file_get_contents('php://stdin');

$allowed_algs = ['HS256', 'HS512', 'HS384'];
try {
    $decoded = JWT::decode($jwt, $key, $allowed_algs);
} catch (Exception $e){
    die("[ERROR] Invalid jwt. Detail: " . $e->getMessage() . "\n");
}

var_dump($decoded);

