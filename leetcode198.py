#!/bin/python
# coding=UTF-8

import unittest

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = len(nums)
        if count == 0 :
            return 0
        elif count == 1 :
            return nums[0]
        elif count == 2 :
            return max(nums[0],nums[1])
        nums[2] += nums[0]
        for i in xrange(3,count):
            #print i, '=' , nums[i], 'after:', (nums[i-3],nums[i-2]) ,
            nums[i] += max(nums[i-3],nums[i-2])
            #print i, '=' , nums[i]

        return max(nums[-1],nums[-2])

class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.rob([]),0)
        self.assertEqual(s.rob([1]),1)
        self.assertEqual(s.rob([1,2]),2)
        self.assertEqual(s.rob([1,3,1]),3)
        self.assertEqual(s.rob([2,1,1,2]),4)
        self.assertEqual(s.rob([2,0,0,0]),2)
        self.assertEqual(s.rob([1,2,3,1]),4)
        self.assertEqual(s.rob([2,7,9,3,1]),12)



if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()

