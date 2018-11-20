#!/bin/python
# coding=UTF-8

import unittest

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def _removeNthFromEnd(self,head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: int count
        """
        if not head:
            return 0
        count = self._removeNthFromEnd(head.next,n)
        if count == n:
            if head.next:
                head.next=head.next.next
        return count + 1

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmp=ListNode(0)
        tmp.next=head
        self._removeNthFromEnd(tmp,n)
        return tmp.next

    def getList(self, head):
        print '[ ',
        result=[]
        if head:
            tmp=head
            while tmp:
                print tmp.val , ' ',
                result.append(tmp.val)
                tmp = tmp.next
        print ']'
        return result

class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        head=ListNode(1)
        n1=ListNode(2)
        n2=ListNode(3)
        n1.next=n2
        head.next=n1
        self.assertEqual(s.getList(head),[1,2,3])
        head=s.removeNthFromEnd(head,1)
        self.assertEqual(s.getList(head),[1,2])
        head=s.removeNthFromEnd(head,2)
        self.assertEqual(s.getList(head),[2])
        head=s.removeNthFromEnd(head,1)
        self.assertEqual(s.getList(head),[])



if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


