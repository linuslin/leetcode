#!/bin/python
# coding=UTF-8

import unittest

class Solution(object):
    strList=[]
    def getStr(self,i,j,count,s):
        if i > 0:
            self.getStr(i-1,j,count+1,s+'(')
        if j > 0 and count > 0 :
            self.getStr(i,j-1,count-1,s+')')
        if i == 0 and j == 0 and count == 0:
            self.strList.append(s)
            #print s

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.strList=[]
        if n <= 0:
            return [""]
        self.getStr(n,n,0,'')
        return self.strList


class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.generateParenthesis(0),[""])
        self.assertEqual(s.generateParenthesis(1),["()"])
        self.assertEqual(s.generateParenthesis(2),["(())","()()"])



if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


