# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def equal(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        left_equal = self.equal(p.left, q.left)
        right_equal = self.equal(p.right, q.right)
        if left_equal and right_equal:
            return True
        return False

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.equal(p, q)


def test_is_same_tree():
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    a.left = b
    a.right = c

    aa = TreeNode(3)
    bb = TreeNode(9)
    cc = TreeNode(20)
    aa.left = bb
    aa.right = cc

    aaa = TreeNode(3)
    bbb = TreeNode(9)
    ccc = TreeNode(21)
    aaa.left = bbb
    aaa.right = ccc

    s = Solution()
    assert s.isSameTree(a, a)
    assert s.isSameTree(a, aa)
