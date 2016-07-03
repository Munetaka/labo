<?php
require('vendor/autoload.php');

use \Firebase\JWT\JWT;

$key = file_get_contents('../../../.ssh/pubkey.pem');

$jwt = file_get_contents('php://stdin');

$allowed_algs = ['RS256'];
try {
    $decoded = JWT::decode($jwt, $key, $allowed_algs);
} catch (Exception $e){
    die("[ERROR] Invalid jwt. Detail: " . $e->getMessage() . "\n");
}

var_dump($decoded);

