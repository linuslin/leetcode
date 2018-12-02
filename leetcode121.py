#!/bin/python
# coding=UTF-8

import unittest
import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        buy = prices[0]
        maxEarn = 0
        for i in xrange(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                maxEarn = max(prices[i] - buy, maxEarn)
        return maxEarn

class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.maxProfit(None),0)
        self.assertEqual(s.maxProfit([]),0)
        self.assertEqual(s.maxProfit([0]),0)
        self.assertEqual(s.maxProfit([0,1]),1)
        self.assertEqual(s.maxProfit([1,0]),0)
        self.assertEqual(s.maxProfit([1,1,1]),0)
        self.assertEqual(s.maxProfit([0,1,2]),2)
        self.assertEqual(s.maxProfit([2,1,0]),0)
        self.assertEqual(s.maxProfit([1,0,2]),2)



if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()

