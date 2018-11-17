#!/bin/python
# coding=UTF-8
import math


class Solution(object):
    def findMaxValue(self, alist, lower, upper):
	print alist, '\n'
        if len(alist)==0:
	    print 'return empty'
        if len(alist)==1:
	    if alist[0] >= lower and alist[0] <= upper:
                return alist[0]
	first = 0
	last = len(alist) -1
	found = False
        result = None
	while first<=last:
	    midpoint = (first + last)//2
	    print 'midpoint', midpoint , alist[midpoint]
	    if alist[midpoint] == lower:
		print 'alist[midpoint] == lower'
		return lower
	    elif alist[midpoint] == upper:
		print 'alist[midpoint] == upper'
		return upper
	    if alist[midpoint] > lower and alist[midpoint] < upper :
		result = alist[midpoint]
		print 'go right'
		print 'alist[midpoint+1:last+1]', midpoint, last
		right = self.findMaxValue(alist[midpoint+1:last+1], lower, upper)
		print 'right=', right
		if right != None:
                    return right
                else:
		    #print 'go left'
		    #left = self.findMaxValue(alist[first:midpoint], lower, upper)
		    #print 'left=', left
	            #if left != None:
                    #    return left
                    #else:
                    return result
		#if left == None and right == None:
		#    print 'left == None and right == None'
		#    return result
		#elif left == None:
		#    print 'left == None'
		#    return result
		#elif right == None:
		#    print 'right == None'
		#    return left
		#print 'else'
		#return left
	    elif lower > alist[midpoint] and alist[midpoint] > upper:
		print 'lower > alist[midpoint] and alist[midpoint] > upper'
		first = midpoint+1
	    elif alist[midpoint] > lower and alist[midpoint] > upper:
		print 'alist[midpoint] > lower and alist[midpoint] > upper'
		last = midpoint-1
            elif lower > alist[midpoint] and alist[midpoint] < upper:
		print 'lower > alist[midpoint] and alist[midpoint] < upper'
		first = midpoint+1
	    else:
		return lower
	return result

    def findMid(self, nums1, nums2):
        lenNums1 = len(nums1)
	lenNums2 = len(nums2)
	#先比較 nums1 nums2 找出偶數序列
	if lenNums1 % 2 == 0:
            idx_1 = lenNums1//2 -1
            idx_2 = lenNums2//2
	    mid_1 = nums1[lenNums1//2 -1 ]
	    mid_2 = nums2[lenNums2//2]
        else:
            idx_1 = lenNums1//2
            idx_2 = lenNums2//2 -1
            mid_1 = nums1[lenNums1//2]
	    mid_2 = nums2[lenNums2//2 -1 ]
        print 'mid_1', mid_1, 'mid_2', mid_2
        # 
	if mid_1 > mid_2:
	    # nums1 mid 最大，找出nums2 右邊部分，中比 mid_1 小 但是比 mid_1 的前個element值大的
	    # 若找不到，中位數就是 mid_1
	    reminder = nums2[lenNums2//2:]
            print 'idx_1 - 1=', idx_1-1
            if idx_1 - 1 < 0:
                return nums2[-1]
	    lower=nums1[idx_1-1] 
	    upper=mid_1
	    #find
            print 'findMax', reminder,lower,upper
	    tmp = self.findMaxValue(reminder,lower,upper)
            print 'tmp=', tmp
	    if tmp == None:
	        #return mid_1
		return lower
            else:
                return tmp
	elif mid_1 == mid_2:
	    # 兩者相等，表示mid_1 mid_2 就是中位數
	    return mid_1
	else: # mid_2 > mid_1
            print 'mid_2> mid_1'
	    # nums2 最大，找出num1 剩餘部分 比mid_2 小但是比 mid_2 的上一個元素大
	    reminder = nums1[lenNums1//2:]
            print 'idx_2 - 1', idx_2 -1
            if (idx_2-1) < 0:
                return nums1[-1]
	    lower=nums2[lenNums2 // 2 - 1]
	    upper=mid_2
            print 'findMax', reminder,lower,upper
	    tmp = self.findMaxValue(reminder,lower,upper)
            print 'tmp=', tmp
	    if tmp == None:
		return mid_2
		#return upper
            else:
		return tmp

    def collection(self, nums1, nums2):
	"""
	:type nums1: List[int]
	:
	:
	"""	
        lenNums1 = len(nums1)
	lenNums2 = len(nums2)
	print '\n\n\n'
	if lenNums1 == lenNums2 == 0:
		return None
	elif lenNums1 == 0:
		return (nums2[lenNums2//2] + nums2[lenNums2//2-1])/2.0 if (lenNums2 % 2) == 0 else nums2[lenNums2//2] 
	elif lenNums2 == 0:
		return (nums1[lenNums1//2] + nums1[lenNums1//2-1])/2.0 if (lenNums1 % 2) == 0 else nums1[lenNums1//2] 
	
        t_cnt = lenNums1+lenNums2
	target = t_cnt/2 + 1 #  make two collection even
	print 'target=', target        #numsList = [ nums1, nums2]
	collected = 0
	tmpCollected = 0
        result = None
	if t_cnt % 2 == 0:
            print 'even'
		# 幫最小的-1
	    if nums1[0] < nums2[0]:
            	mid_1 = self.findMid(nums1[1:],nums2)
	    else:
            	mid_1 = self.findMid(nums1,nums2[1:])
		#幫最大的+1
            print 'mid_1' , mid_1
	    if nums1[-1] > nums2[-1]:
                mid_2 = self.findMid(nums1[:-1],nums2)
                #mid_2 = self.findMid([nums1,nums1[:-1]+1],nums2)
	    else:
		print nums2[:-1]
                mid_2 = self.findMid(nums1,nums2[:-1])
                #mid_2 = self.findMid(nums1,[nums2,nums2[-1]+1])
            print 'mid_2' , mid_2
	    return (mid_1+mid_2)/2.0

	else:
	    return self.findMid(nums1, nums2)

import unittest
class TestMethods(unittest.TestCase):
    def test_upper(self):
	s=Solution()
        #self.assertEqual(s.collection([1,3],[2]),2.0)
        #self.assertEqual(s.sort2([1,2],[3,4]),2.5)
        #self.assertEqual(s.collection([1,2,5],[3,4]),3)
        #self.assertEqual(s.collection([2,4],[1,3,5]),3)
        #self.assertEqual(s.collection([2,4],[1,3]),2.5)
        self.assertEqual(s.collection([1,2,3],[4,5,6]),3.5)
        #self.assertEqual(s.collection([1,2,3],[4,5]),3)
        #print [2,4,6,8,10]
        #self.assertEqual(s.findMaxValue([2,4,6,8,10],4,9),4)
        #print [12,14,16,18,20]
        self.assertEqual(s.findMaxValue([12,14,16,18,20],4,9),None)
        self.assertEqual(s.findMaxValue([12,14,16,18,20],4,9),None)
        self.assertEqual(s.findMaxValue([1,2,3],0,4),3)
        self.assertEqual(s.findMaxValue([1,2,3,5],0,4),3)
	#print [6,14,16,18,20]
        #self.assertEqual(s.findMaxValue([6,14,16,18,20],4,9),6)
        #self.assertEqual(s.findMedianSortedArrays([1,3],[2]),2.0)
        #self.assertEqual(s.findMedianSortedArrays([1,2],[3,4]),2.5)

if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


