#!/usr/bin/python3

import unittest
from calc_mul import calc

class TestCalc (unittest.TestCase):

        # --- 有効同値・境界値テスト ---
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))
        
        def test_sample2 (self):
                self.assertEqual (1, calc(1,1))

        def test_sample3 (self):
                self.assertEqual (998001, calc(999,999))

        # --- 無効同値・境界値外テスト ---
        def test_sample4 (self):
                self.assertEqual (-1, calc(0,1))

        def test_sample5 (self):
                self.assertEqual (-1, calc(1,1000))

        # --- 無効同値・型エラーテスト ---
        def test_sample6 (self):
                self.assertEqual (-1, calc(0.1,999))

        def test_sample7 (self):
                self.assertEqual (-1, calc("a",1))

        def test_sample8 (self):
                self.assertEqual (-1, calc("1","2"))

        def test_sample9 (self):
                self.assertEqual (-1, calc(None,1))