<?php

class BenchMark
{
    private function __construct() {}
    public static function run($class, $exec_cnt = 10)
    {
        if (!is_object($class)) {
            $class = new $class();
        }

        echo str_pad('-', 38, '-'), "\n";
        echo '|', str_pad('benchmark start', 36, ' ', STR_PAD_BOTH), "|\n";
        echo str_pad('-', 38, '-'), "\n";
        $start = microtime(true);
        foreach (get_class_methods($class) as $method) {
            if ($method == '__construct') {
                continue;
            }
            echo str_pad($method, 25), ':';
            $start_method = microtime(true);
            $i = 0;
            while ($i <= $exec_cnt) {
                $class->$method();
                ++$i;
            }
            $end_method = microtime(true);
            echo sprintf('%.5f', $end_method - $start_method), " sec\n";
        }
        $end = microtime(true);
        echo str_pad('-', 38, '-'), "\n";
        echo str_pad('Total time', 25), ':', sprintf('%.5f', $end - $start), " sec\n\n\n";
    }
}
