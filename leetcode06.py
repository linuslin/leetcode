import math

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
	if numRows <= 1 :
		return s

	strs = ["" for x in range(numRows)]
	bound = 2 * ( numRows -1 )
	for i in xrange(len(s)):
		mod=i%bound
		if mod >= numRows:
			mod = bound - mod
		strs [mod] += s[i]
	result = ''
	for str in strs:
		result += str
	return result
 

import unittest
class TestMethods(unittest.TestCase):
    def test_upper(self):
	s=Solution()
        self.assertEqual(s.convert(s = "PAYPALISHIRING", numRows = 1),'PAYPALISHIRING')
        self.assertEqual(s.convert(s = "PAYPALISHIRING", numRows = 2),'PYAIHRNAPLSIIG')
        self.assertEqual(s.convert(s = "PAYPALISHIRING", numRows = 3),'PAHNAPLSIIGYIR')
        self.assertEqual(s.convert(s = "PAYPALISHIRING", numRows = 4),'PINALSIGYAHRPI')

if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


