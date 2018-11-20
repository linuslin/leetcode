import math


class Solution(object):
    def reverseNum(self, num):
        if num < 0:
            sign = -1
            num *= sign
        else:
            sign=1
        tmp=0
        while ( num > 0):
            tmp = tmp * 10 + (num % 10)
            num /= 10
        return tmp*sign

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
        if x == 0:
            return True
        modX = x % 10
        if modX == 0:
            return False
        r_x = self.reverseNum(x)
        if r_x != x:
            return False
        return True

import unittest
class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.reverseNum(123),321)
        self.assertEqual(s.reverseNum(-123),-321)
        self.assertEqual(s.reverseNum(120),21)
        self.assertEqual(s.reverseNum(1023456789),9876543201)
        self.assertEqual(s.reverseNum(7463847412),2147483647)
        self.assertEqual(s.reverseNum(2147483647),7463847412)
        self.assertEqual(s.reverseNum(-2147483648),-8463847412)
        self.assertEqual(s.reverseNum(-8463847412),-2147483648)
        self.assertEqual(s.isPalindrome(-8463847412),False)
        self.assertEqual(s.isPalindrome(1),True)
        self.assertEqual(s.isPalindrome(0),True)
        self.assertEqual(s.isPalindrome(10),False)
        self.assertEqual(s.isPalindrome(121),True)

if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


