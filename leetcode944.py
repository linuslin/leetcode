#!/bin/python
# coding=UTF-8

import unittest

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        count = 0
        for zips in zip(*A):
            print zips
            for i in xrange(len(zips) - 1):
                if zips[i] > zips[i+1]:
                    count += 1
                    break
        return count
        # sum(list(col) != sorted(col) for col in zip(*A))

class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.minDeletionSize(["cba","daf","ghi"]),1)
        self.assertEqual(s.minDeletionSize(["a","b"]),0)
        self.assertEqual(s.minDeletionSize(["zyx","wvu","tsr"]),3)
        self.assertEqual(s.minDeletionSize([]),0)


if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


