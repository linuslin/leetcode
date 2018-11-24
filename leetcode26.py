#!/bin/python
# coding=UTF-8

import unittest

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
	if not nums:
            return 0
        if len(nums) <= 1:
            return len(nums)
        end = 0
        for i in range(1, len(nums)):
            if nums[end] != nums[i]:
                end += 1
                nums[end] = nums[i]

        end += 1
        nums[:]=nums[:end]
        return end

class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        nums=None
        self.assertEqual(s.removeDuplicates(nums),0)
        self.assertEqual(nums,None)
        nums=[]
        self.assertEqual(s.removeDuplicates(nums),0)
        self.assertEqual(nums,[])
        nums=[1]
        self.assertEqual(s.removeDuplicates(nums),1)
        self.assertEqual(nums,[1])
        nums=[-1,-1]
        self.assertEqual(s.removeDuplicates(nums),1)
        self.assertEqual(nums,[-1])
        nums=[-1,-1,0]
        self.assertEqual(s.removeDuplicates(nums),2)
        self.assertEqual(nums,[-1,0])


if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


