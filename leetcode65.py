def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        rs=re.sub('^[\s]*', '', s.lower())
        rs=re.sub('$[\s]*', '', rs)
	print rs
        return is_number(rs)
        

import unittest
class TestMethods(unittest.TestCase):
    def test_upper(self):
	s=Solution()
        #self.assertEqual('foo'.upper(), 'FOO')
        self.assertTrue(s.isNumber('2'))
        self.assertTrue(s.isNumber(' 2.143'))
        self.assertTrue(s.isNumber(' 0.1 '))
        self.assertTrue(s.isNumber(' 2e10 '))
        self.assertTrue(s.isNumber(' -1.05E+003 '))
        self.assertFalse(s.isNumber('abc'))
        self.assertFalse(s.isNumber('1 a'))
        self.assertFalse(s.isNumber('. 1'))
        self.assertFalse(s.isNumber('+ 1'))

if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


