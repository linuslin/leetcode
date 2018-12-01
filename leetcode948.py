#!/bin/python
# coding=UTF-8

import unittest

class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        if not tokens:
            return 0
        scores = 0
        tokens.sort()
        top = 0
        tail = len(tokens)-1
        max_ans = 0
        while tail >= top:
            while tail >= top and P >= tokens[top]:
                P -= tokens[top]
                scores += 1
                top += 1
                if scores > max_ans:
                    max_ans = scores
            if scores > 0:
                scores -= 1
                P += tokens[tail]
                tail -= 1
            else:
                break
        return max_ans


class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.bagOfTokensScore([100],50),0)
        self.assertEqual(s.bagOfTokensScore([400,200,100,100],200),2)
        self.assertEqual(s.bagOfTokensScore([100,200],150),1)
        self.assertEqual(s.bagOfTokensScore([100,200,300,400],200),2)


if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


