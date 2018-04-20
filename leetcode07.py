import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """ 
	isNeg=x<0
	rStr=str(abs(x))[::-1]
        result = int(rStr)
        Neg_int32Max = -0x80000000
        int32Max =      0x7fffffff
	if isNeg:
		if (-result & Neg_int32Max == Neg_int32Max):
			return -result 	
		return 0
	else:
		if (result == int32Max & result):
			return result
		return 0
	

import unittest
class TestMethods(unittest.TestCase):
    def test_upper(self):
	s=Solution()
        self.assertEqual(s.reverse(123),321)
        self.assertEqual(s.reverse(-123),-321)
        self.assertEqual(s.reverse(120),21)
        self.assertEqual(s.reverse(1023456789),0)
        self.assertEqual(s.reverse(7463847412),2147483647)
        self.assertEqual(s.reverse(2147483647),0)
        self.assertEqual(s.reverse(-2147483648),0)
        self.assertEqual(s.reverse(-8463847412),-2147483648)

if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


