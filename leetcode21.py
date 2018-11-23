#!/bin/python
# coding=UTF-8

import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def dumpList(self, nums):
        tmp = []
        itor = nums
        while itor:
            print itor.val
            tmp.append(itor.val)
            itor=itor.next
        return tmp

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #if not l1:
        #    return l2
        #if not l2:
        #    return l1

        head = ListNode(0)
        itor = head
        while l1 and l2:
            if l1.val < l2.val:
                itor.next = l1
                itor=l1
                l1 = l1.next
            else:
                itor.next = l2
                itor=l2
                l2 = l2.next
        if l1:
            itor.next = l1
        if l2:
            itor.next = l2
        return head.next


class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        l1=None
        l2=None
        rst=None
        self.assertEqual(s.dumpList(s.mergeTwoLists(l1,l2)),s.dumpList(rst))
        l1=ListNode(-1)
        self.assertEqual(s.dumpList(s.mergeTwoLists(l1,l2)),s.dumpList(l1))
        self.assertEqual(s.dumpList(s.mergeTwoLists(l2,l1)),s.dumpList(l1))
        l2=ListNode(-1)
        rst=ListNode(-1)
        rst.next=ListNode(-1)
        self.assertEqual(s.dumpList(s.mergeTwoLists(l1,l2)),s.dumpList(rst))
        rst.next.next=ListNode(0)
        rst.next.next.next=ListNode(1)
        l2.next=ListNode(0)
        l1.next=ListNode(1)
        self.assertEqual(s.dumpList(s.mergeTwoLists(l1,l2)),s.dumpList(rst))


if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


