#!/bin/python
# coding=UTF-8

import unittest
import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        maxsum = nums[0]
        for i in xrange(1,len(nums)):
            nums[i] += max(nums[i-1],0)
            if nums[i] > maxsum:
                maxsum = nums[i]
        return maxsum

class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.maxSubArray(None),None)
        self.assertEqual(s.maxSubArray([]),None)
        self.assertEqual(s.maxSubArray([-1]),-1)
        self.assertEqual(s.maxSubArray([0]),0)
        self.assertEqual(s.maxSubArray([1,2]),3)
        self.assertEqual(s.maxSubArray([-1,1,2,-1]),3)
        self.assertEqual(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]),6)



if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()

