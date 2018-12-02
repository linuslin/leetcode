#!/bin/python
# coding=UTF-8

import unittest
import sys

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sumCache = nums;
        for i in xrange(1,len(nums)):
            self.sumCache[i] += self.sumCache[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # TODO:check boundary
        low = i -1
        if low < 0:
            return self.sumCache[j]
        return self.sumCache[j] - self.sumCache[low]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

class TestMethods(unittest.TestCase):
    def test_upper(self):
        nums = [-2, 0, 3, -5, 2, -1]
        numArr = NumArray(nums)
        self.assertEqual(numArr.sumRange(0,2),1)
        self.assertEqual(numArr.sumRange(2,5),-1)
        self.assertEqual(numArr.sumRange(0,5),-3)


if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()

