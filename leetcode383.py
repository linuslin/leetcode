#!/bin/python
# coding=UTF-8

import unittest

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        print "================"
        if num < 0:
            return None
        if num == 0:
            return [0]
        tmp=[0]
        times=0
        base=0
        bound=1
        for i in xrange(1,num+1):
            print 'index:' , i
            if i == bound:
                tmp.append(1)
                times += 1
                base = bound
                bound = pow(2,times)
            else:
                tmp.append(1 + tmp[i-base])

        return tmp

class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        self.assertEqual(s.countBits(0),[0])
        self.assertEqual(s.countBits(1),[0,1])
        self.assertEqual(s.countBits(2),[0,1,1])
        self.assertEqual(s.countBits(3),[0,1,1,2])
        self.assertEqual(s.countBits(4),[0,1,1,2,1])
        self.assertEqual(s.countBits(5),[0,1,1,2,1,2])
        self.assertEqual(s.countBits(6),[0,1,1,2,1,2,2])



if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


