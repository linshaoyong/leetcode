# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if L > root.val:
            return self.trimBST(root.right, L, R)
        elif R < root.val:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root


def test_trim_bst_1():
    s = Solution()
    a = TreeNode(1)
    b = TreeNode(0)
    c = TreeNode(2)
    a.left = b
    a.right = c

    aa = s.trimBST(a, 1, 2)
    assert 1 == aa.val
    assert aa.left is None
    assert 2 == aa.right.val
    assert aa.right.left is None
    assert aa.right.right is None


def test_trim_bst_2():
    s = Solution()
    a = TreeNode(3)
    b = TreeNode(0)
    c = TreeNode(4)
    d = TreeNode(2)
    e = TreeNode(1)
    a.left = b
    a.right = c
    b.right = d
    d.left = e

    aa = s.trimBST(a, 1, 3)
    assert 3 == aa.val
    assert aa.right is None
    assert 2 == aa.left.val
    assert aa.left.right is None
    assert 1 == aa.left.left.val
    assert aa.left.left.left is None
    assert aa.left.left.right is None
