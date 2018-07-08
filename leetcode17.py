#!/bin/python
# coding=UTF-8

import math
import unittest

class Solution(object):
	def appendLetters(self, strs, str2):
		"""
		:type strs: List[str]
		:type str2: str
		:rtype: List[str]
		"""
		result = []
		for s in strs:
			for s2 in str2:
				result.append(s+s2)
		return result

	def letterCombinations(self, digits):
		"""
        :type digits: str
        :rtype: List[str]
        """
		digitDict = { '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz' }
		result = ['']
		for digit in digits:
			if digit in digitDict:
				result = self.appendLetters(result, digitDict[digit])
		if len(result) <= 1:
			return []
		return result

class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.letterCombinations('1'),[])
        self.assertEqual(s.letterCombinations('0'),[])
        self.assertEqual(s.letterCombinations('2'),["a", "b", "c"])
        self.assertEqual(s.letterCombinations('02'),["a", "b", "c"])
        self.assertEqual(s.letterCombinations('20'),["a", "b", "c"])
        self.assertEqual(s.letterCombinations('3'),["d", "e", "f"])
        self.assertEqual(s.letterCombinations('4'),["g", "h", "i"])
        self.assertEqual(s.letterCombinations('5'),["j", "k", "l"])
        self.assertEqual(s.letterCombinations('23'),["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        self.assertEqual(s.letterCombinations('789'),['ptw','ptx','pty','ptz','puw','pux','puy','puz','pvw','pvx','pvy','pvz','qtw','qtx','qty','qtz','quw','qux','quy','quz','qvw','qvx','qvy','qvz','rtw','rtx','rty','rtz','ruw','rux','ruy','ruz','rvw','rvx','rvy','rvz','stw','stx','sty','stz','suw','sux','suy','suz','svw','svx','svy','svz'])


if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


