import math

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num1_len=len(nums1)
	num2_len=len(nums2)
	if num1_len <= 0 and num2_len <= 0:
		return
	if num1_len <= 0:
		return (nums2[int(math.ceil(num2_len/2.0 - 1))] + nums2[int(num2_len/2)] ) / 2.0
	if num2_len <= 0:      
		return (nums1[int(math.ceil(num1_len/2.0 - 1))] + nums1[int(num1_len/2)] ) / 2.0
	



	return 0

import unittest
class TestMethods(unittest.TestCase):
    def test_upper(self):
	s=Solution()
        self.assertEqual(s.findMedianSortedArrays([1,2],[]),1.5)
        self.assertEqual(s.findMedianSortedArrays([1],[]),1)
        self.assertEqual(s.findMedianSortedArrays([],[1,2]),1.5)
        self.assertEqual(s.findMedianSortedArrays([],[1]),1)
        self.assertEqual(s.findMedianSortedArrays([1,2,3],[]),2)
        self.assertEqual(s.findMedianSortedArrays([],[1,2,3]),2)
        self.assertEqual(s.findMedianSortedArrays([],[]),None)
        self.assertEqual(s.findMedianSortedArrays([1,3],[2]),2.5)

if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


