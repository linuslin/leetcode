#!/bin/python
# coding=UTF-8

import unittest


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result=self.inorderTraversal(root.left)+ [root.val] + self.inorderTraversal(root.right)
        return result


class TestMethods(unittest.TestCase):
    def test_upper(self):
        s=Solution()
        n3=TreeNode(3)
        n2=TreeNode(2)
        n1=TreeNode(1)
        self.assertEqual(s.inorderTraversal(n3),[3])
        self.assertEqual(s.inorderTraversal(None),[])
        n3.left=n2
        self.assertEqual(s.inorderTraversal(n3),[2,3])
        n2.right=n1
        self.assertEqual(s.inorderTraversal(n3),[2,1,3])



if __name__ == '__main__':
    # creates an instance of the class
    unittest.main()


