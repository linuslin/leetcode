#!/bin/python
# coding=UTF-8

import math
import unittest

class Solution(object):
	def maxArea(self, height):
		"""
    	:type height: List[int]
    	:rtype: int
    	"""
		count = len(height)
		if count < 1 :
			return 0
		last = count - 1
		first = 0
		maxArea = 0
		while (first!=last):
			waterMinH = min(height[first],height[last])
			tmpArea = waterMinH * (last - first)
			if tmpArea > maxArea:
				maxArea = tmpArea
			if height[first] > height[last]:
				last -= 1
			else:
				first += 1
		return maxArea

class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.maxArea([2,3,4,5]),6)
        self.assertEqual(s.maxArea([4,3,2,5]),12)
        self.assertEqual(s.maxArea([4,3,2,1]),4)
        self.assertEqual(s.maxArea([]),0)
        self.assertEqual(s.maxArea([1]),0)
        self.assertEqual(s.maxArea([6,3,2,6]),18)
        self.assertEqual(s.maxArea([1,2,1]),2)

if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


