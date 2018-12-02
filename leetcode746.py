#!/bin/python
# coding=UTF-8

import unittest
import sys

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost or len(cost) < 2 :
            return 0
        count = len(cost)
        for i in xrange(2,count):
            cost[i] += min(cost[i-2],cost[i-1])
        return min(cost[count-2],cost[count-1])

class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.minCostClimbingStairs(None),0)
        self.assertEqual(s.minCostClimbingStairs([]),0)
        self.assertEqual(s.minCostClimbingStairs([0]),0)
        self.assertEqual(s.minCostClimbingStairs([0,1]),0)
        self.assertEqual(s.minCostClimbingStairs([10, 15, 20]),15)
        self.assertEqual(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]),6)



if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()

