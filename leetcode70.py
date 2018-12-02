#!/bin/python
# coding=UTF-8

import unittest
import sys

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 0 ans = 1 but I think this proble should be 1
        if n == 0:
            return 1
        # n = 0 return 0 , ... n = 2 return 2
        if n < 3:
            return n 
        #return self.climbStairs(n-1)+self.climbStairs(n-2)
        prevprev = 1
        prev = 2
        # iterate at least once so 3-1 = 2  
        for i in xrange(2,n):
            tmp = prev+prevprev
            prevprev = prev
            prev = tmp
        return prev

class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.climbStairs(0),1)
        self.assertEqual(s.climbStairs(1),1)
        self.assertEqual(s.climbStairs(2),2)
        self.assertEqual(s.climbStairs(3),3)
        self.assertEqual(s.climbStairs(4),5)
        self.assertEqual(s.climbStairs(5),8)



if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()

