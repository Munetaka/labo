<?php
require_once dirname(__FILE__) . '/benchmark.php';

class forWhile
{
    private $_calc_count = 100000;

    public function forLoop()
    {
        $count = 0;
        for ($i = 0; $i <= $this->_calc_count; ++$i) {
            ++$count;
        }
    }

    public function whileLoop()
    {
        $i = 0;
        $count = 0;
        while ($i <= $this->_calc_count) {
            ++$count;
            ++$i;
        }
    }
}

Benchmark::run('forWhile', 100);
