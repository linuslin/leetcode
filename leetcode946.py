#!/bin/python
# coding=UTF-8

import unittest

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type poped: List[int]
        :rtype: bool
        """
        if pushed and popped:
            stack = []
            count = 0
            for x in pushed:
                stack.append(x)
                while stack and stack[-1] == popped[count]:
                    count += 1
                    stack.pop()
            return count == len(popped)
        return pushed == popped

class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.validateStackSequences([1,2,3,4,5],[4,5,3,2,1]),True)
        self.assertEqual(s.validateStackSequences([1,2,3,4,5],[4,3,5,1,2]),False)
        self.assertEqual(s.validateStackSequences([1,2],[2,1]),True)
        self.assertEqual(s.validateStackSequences([1,2],[1,2]),True)
        self.assertEqual(s.validateStackSequences([],[]),True)
        self.assertEqual(s.validateStackSequences(None,None),True)


if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


