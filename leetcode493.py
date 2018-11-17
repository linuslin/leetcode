#!/bin/python
# coding=UTF-8

import math
import unittest

class Solution(object):
    def __init__(self):
        sortedList = []
    def findSmallersCounts(self, value):
        """
        :type nums: sorted List[int]
        :rtype: int
        """
        count = 0
        first = 0
        last = len(self.sortedList) - 1
        #print "first ", first, " last ", last 
        #if last < 0:
        #    return 0
        #if nums[last] < value:
        #    return last + 1
        while first <= last :
            midpoint = (first + last)//2
            #print 'mid:', midpoint,'first:', first, '(',nums[first],') last:',last, '(' ,nums[last],')' 
            if self.sortedList[midpoint] < value:
                #print '<'
                first = midpoint + 1
                count = first
            else:
                #print '>='
                last = midpoint - 1
        return count

# 0.053s ~ 0.054s
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.sortedList = []
        if len(nums) < 2 :
            return 0
        count = 0
        for element in nums:
            count += len(self.sortedList) - self.findSmallersCounts(element*2 + 1)
            index = self.findSmallersCounts(element)
            self.sortedList.insert(index,element)
        return count
#2.001s
    def reversePairsOld(self, nums):
        count=0
        for i in xrange(len(nums)):
            for j in xrange(i+1,len(nums)):
                if nums[i] > nums[j] * 2:
                    count +=1
        return count

class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        #self.assertEqual(s.findSmallersCounts([],0),0)
        #self.assertEqual(s.findSmallersCounts([1],1),0)
        #self.assertEqual(s.findSmallersCounts([1],0),0)
        #self.assertEqual(s.findSmallersCounts([1],2),1)
        #self.assertEqual(s.findSmallersCounts([1,2],0),0)
        #self.assertEqual(s.findSmallersCounts([1,2],1),0)
        #self.assertEqual(s.findSmallersCounts([1,2],2),1)
        #self.assertEqual(s.findSmallersCounts([1,2],3),2)
        #self.assertEqual(s.findSmallersCounts([1,1,2,2,3],3),4)
        #self.assertEqual(s.reversePairs([1,3,2,3,1]),2)
        #self.assertEqual(s.reversePairs([2,4,3,5,1]),3)
        #self.assertEqual(s.reversePairs([]),0)
        #self.assertEqual(s.reversePairs([1]),0)
        #self.assertEqual(s.reversePairs([4,4,1]),2)
        #self.assertEqual(s.reversePairs([4,1,4,1]),3)
        self.assertEqual(s.reversePairs(range(1,5000)),0)
        self.assertEqual(s.reversePairs(list(reversed(range(1,5000)))),6245001)


if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


