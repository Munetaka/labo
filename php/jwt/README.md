JWT-php encode/decode test
========

setup
--------
Use composer to manage dependencies and download
```bash
composer install
```

Example
--------
```bash
$ echo '{"key1":"value1","expire":12345}' | php encode.php
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrZXkxIjoidmFsdWUxIiwiZXhwaXJlIjoxMjM0NX0.-Bo48Q1XfqzyeVtp7q_I64wizn6xYGOwuASMlDtIzl4
```
```bash
$ echo '{"key1":"value1","expire":12345}' | php encode.php | php decode.php
object(stdClass)#3 (2) {
  ["key1"]=>
  string(6) "value1"
  ["expire"]=>
  int(12345)
}
```
