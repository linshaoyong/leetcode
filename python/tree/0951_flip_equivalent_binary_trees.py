# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is None:
            return root2 is None
        if root2 is None:
            return root1 is None
        if root1.val != root2.val:
            return False
        if self.flipEquiv(root1.left, root2.left) and \
                self.flipEquiv(root1.right, root2.right):
            return True
        if self.flipEquiv(root1.left, root2.right) and \
                self.flipEquiv(root1.right, root2.left):
            return True
        return False


def test_flip_equiv():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    h = TreeNode(8)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    e.left = g
    e.right = h

    aa = TreeNode(1)
    bb = TreeNode(3)
    cc = TreeNode(2)
    dd = TreeNode(6)
    ee = TreeNode(4)
    ff = TreeNode(5)
    gg = TreeNode(8)
    hh = TreeNode(7)
    aa.left = bb
    aa.right = cc
    bb.right = dd
    cc.left = ee
    cc.right = ff
    ff.left = gg
    ff.right = hh

    assert Solution().flipEquiv(a, aa)
