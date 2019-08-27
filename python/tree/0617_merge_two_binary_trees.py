# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


def test_merge_trees():
    s = Solution()

    a = TreeNode(1)
    b = TreeNode(3)
    c = TreeNode(2)
    d = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d

    aa = TreeNode(2)
    bb = TreeNode(1)
    cc = TreeNode(3)
    dd = TreeNode(4)
    ee = TreeNode(7)
    aa.left = bb
    aa.right = cc
    bb.right = dd
    cc.right = ee

    root = s.mergeTrees(a, aa)
    assert 3 == root.val
    assert 4 == root.left.val
    assert 5 == root.right.val
    assert 5 == root.left.left.val
    assert 4 == root.left.right.val
    assert 7 == root.right.right.val
