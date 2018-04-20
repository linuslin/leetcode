class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
	n=len(nums) 
	if n < 1:
	    return 0
	max=1
        numsSet=set(nums)
	for i in numsSet:
	    if i - 1 not in numsSet:
            	inc=1
	    	while (i+inc) in numsSet:
	            inc+=1
	            if (inc>max):
		        max=inc
        return max
        

import unittest
class TestMethods(unittest.TestCase):
    def test_upper(self):
	s=Solution()
        #self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual(s.longestConsecutive([100, 4, 200, 1, 3, 2]),4)
        self.assertEqual(s.longestConsecutive([0]),1)
        self.assertEqual(s.longestConsecutive([9,8,7,6,5,4,3,2,1,0]),10)

if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


