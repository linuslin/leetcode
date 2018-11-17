#!/bin/python
# coding=UTF-8

import math
import unittest

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        count = len(strs)
        if not count:
            return ''
        if count == 1:
            return strs[0]
        index = 0
        result = ''
        while True:
            kStr=''
            for i in xrange(len(strs)) :
                if len(strs[i]) > index:
                    if not kStr:
                        kStr=strs[i][index]
                        continue
                    if strs[i][index] != kStr:
                        return result
                else:
                    return result
            index += 1
            result += kStr


class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.longestCommonPrefix([]),'')
        self.assertEqual(s.longestCommonPrefix(['']),'')
        self.assertEqual(s.longestCommonPrefix(['','']),'')
        self.assertEqual(s.longestCommonPrefix(['1','1']),'1')
        self.assertEqual(s.longestCommonPrefix(['1','2']),'')
        self.assertEqual(s.longestCommonPrefix(['123']),'123')
        self.assertEqual(s.longestCommonPrefix(['123','12','1']),'1')
        self.assertEqual(s.longestCommonPrefix(['12','1','']),'')
        self.assertEqual(s.longestCommonPrefix(["dog","racecar","car"]),'')
        self.assertEqual(s.longestCommonPrefix(["flower","flow","flight"]),'fl')


if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


