#!/bin/python
# coding=UTF-8

import unittest

class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int] : 0 <= A.length <= 40000; 0 <= A[i] < 40000
        :rtype: int
        """
        # sort 資料
        # 每次可以塞的資料都是前次值的 + 1 或是已插入值(nextInt)的 +1
        # 所以差距相當於 nextInt - val (現在值)
        count = nextInt = 0
        for val in sorted(A):
            count += max(nextInt - val, 0)
            nextInt = max(nextInt + 1, val + 1)
        return count

class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.minIncrementForUnique([1,2,2]),1)
        self.assertEqual(s.minIncrementForUnique([3,2,1,2,1,7]),6)
        self.assertEqual(s.minIncrementForUnique([0]),0)
        self.assertEqual(s.minIncrementForUnique([]),0)



if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()

