#!/bin/python
# coding=UTF-8

import unittest

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]] 
        :rtype: int
        """
        if not costs:
            return 0
        count = len(costs)
        for i in xrange(1,count):
            costs[i][0] += min(costs[i-1][1],costs[i-1][2])
            costs[i][1] += min(costs[i-1][0],costs[i-1][2])
            costs[i][2] += min(costs[i-1][0],costs[i-1][1])
        print costs[count-1]
        return min(costs[count-1])




class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.minCost([]),0)
        self.assertEqual(s.minCost([[1,2,3],[3,2,1],[2,2,2]]),4)



if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()

