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
        maxEarn = 0
        buy = sell = prices[0]
        trans = False
        for i in xrange(1,len(prices)):
            if sell > prices[i]:
                #clear transaction
                maxEarn += sell - buy
                buy = sell = prices[i]
            else:
                sell = prices[i]
        return maxEarn + sell - buy


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
        self.assertEqual(s.maxProfit([7,1,5,3,6,4]),7)
        self.assertEqual(s.maxProfit([1,2,3,4,5]),4)
        self.assertEqual(s.maxProfit([7,6,4,3,1]),0)
        self.assertEqual(s.maxProfit([1,5,6,1,7]),11)



if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()

