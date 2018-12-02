#!/bin/python
# coding=UTF-8

import unittest
import sys

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]] 
        :rtype: int
        """
        if not costs:
            return 0
        count = len(costs)
        prevMin = prev2ndMin = 0
        prevMinIdx = None
        for i in xrange(count):
            currMin = curr2ndMin = sys.maxint
            currMinIdx = None
            for j in xrange(len(costs[i])):
                if j == prevMinIdx:
                    costs[i][j] += prev2ndMin
                else:
                    costs[i][j] += prevMin
                if costs[i][j] < currMin:
                    curr2ndMin = currMin
                    currMin = costs[i][j]
                    currMinIdx = j
                elif costs[i][j] < curr2ndMin:
                    curr2ndMin = costs[i][j]
            prevMin = currMin
            prev2ndMin = curr2ndMin
            prevMinIdx = currMinIdx

        return currMin




class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.minCostII([]),0)
        self.assertEqual(s.minCostII([[1,2,3],[3,2,1],[2,2,2]]),4)
        self.assertEqual(s.minCostII([[1,2,3,4],[4,3,2,1],[1,2,3,4]]),3)



if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()

