# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
import unittest
from SonarQube import review_rate


class TestStringMethods(unittest.TestCase):



    def test_case_01(self):
        count_number = review_rate.count_number(2)
        self.assertEqual(count_number, 2)

    def test_case_02(self):
        count_str = review_rate.count_str("test")
        self.assertEqual(count_str,"test")

if __name__ == '__main__':
    unittest.main()

