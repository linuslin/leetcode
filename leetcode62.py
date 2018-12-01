#!/bin/python
# coding=UTF-8

import unittest

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        if m == 1 or n ==1:
            return 1
        # (m+n)! / m!n!
        if m > n :
            up = m - 1
            low = n - 1
        else:
            up = n - 1
            low = m - 1

        div = divider = 1

        for i in xrange(up+1,low+up+1):
            div *= i
        for i in xrange(1,low+1):
            divider *= i
        return div/divider

class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.uniquePaths(0,0),0)
        self.assertEqual(s.uniquePaths(1,0),0)
        self.assertEqual(s.uniquePaths(0,1),0)
        self.assertEqual(s.uniquePaths(1,1),1)
        self.assertEqual(s.uniquePaths(10,1),1)
        self.assertEqual(s.uniquePaths(1,10),1)
        self.assertEqual(s.uniquePaths(3,2),3)
        self.assertEqual(s.uniquePaths(7,3),28)



if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()

