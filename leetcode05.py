import math

class Solution(object):
    def isPalindrome(self,s):
	#print s, ':', s[::-1] 
       	#return s==s[::-1]
	s_len = len(s)
        for index in range(s_len/2):
		if (s[index] != s[s_len-1-index]):
			return False
	return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
	if len(s) <= 1 :
		return s
        begin=0
	maxLen=1
	for i in xrange(len(s)):
                # print "i=", i, " maxLen=", maxLen 
		# "xVx"
		if i >= (maxLen + 1) and self.isPalindrome(s[i-(maxLen+1):i+1]):
			begin = i-(maxLen+1)
			maxLen += 2
		# "xx"
		elif i >= maxLen and self.isPalindrome(s[i-maxLen:i+1]):
			begin = i-maxLen
			maxLen += 1 
	#print "begin=", begin ," maxLen=",maxLen
	return s[begin:begin+maxLen]

import unittest
class TestMethods(unittest.TestCase):
    def test_upper(self):
	s=Solution()
        self.assertEqual(s.isPalindrome(''),True)
        self.assertEqual(s.isPalindrome('A'),True)
        self.assertEqual(s.isPalindrome('AB'),False)
        self.assertEqual(s.isPalindrome('ABA'),True)
        self.assertEqual(s.longestPalindrome('ABA'),'ABA')
        self.assertEqual(s.longestPalindrome('AB'),'A')
        self.assertEqual(s.longestPalindrome('ABACACA'),'ACACA')
        self.assertEqual(s.longestPalindrome('ACACABA'),'ACACA')
        self.assertEqual(s.longestPalindrome("babaddtattarrattatddetartrateedredividerb"),'ddtattarrattatdd')

if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


