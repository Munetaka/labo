<?php
require_once dirname(__FILE__) . '/benchmark.php';

class IncrementDecrement
{
    private $_calc_count = 100000;

    public function roopAfterCountAfter()
    {
        $count = 0;
        for ($i = 0; $i <= $this->_calc_count; $i++) {
            $count++;
        }
    }

    public function roopAfterCountBefore()
    {
        $count = 0;
        for ($i = 0; $i <= $this->_calc_count; $i++) {
            ++$count;
        }
    }

    public function roopBeforeCountAfter()
    {
        $count = 0;
        for ($i = 0; $i <= $this->_calc_count; ++$i) {
            $count++;
        }
    }

    public function roopBeforeCountBefore()
    {
        $count = 0;
        for ($i = 0; $i <= $this->_calc_count; ++$i) {
            ++$count;
        }
    }
}

Benchmark::run('IncrementDecrement', 100);
