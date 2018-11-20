#!/bin/python
# coding=UTF-8

import unittest

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        symbol = {'{':1,'}':-1,'[':2,']':-2,'(':3,')':-3}
        stack = []
        for x in s:
            i = symbol[x]
            if i > 0:
                stack.append(x)
            else:
                if not stack or symbol[stack.pop()] + i != 0:
                    return False
        return not stack


class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.isValid(''),True)
        self.assertEqual(s.isValid('()'),True)
        self.assertEqual(s.isValid('()[]{}'),True)
        self.assertEqual(s.isValid('(]'),False)
        self.assertEqual(s.isValid('([)]'),False)
        self.assertEqual(s.isValid('{[]}'),True)
        self.assertEqual(s.isValid('}'),False)



if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


