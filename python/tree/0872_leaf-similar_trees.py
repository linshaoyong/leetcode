# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        r1, r2 = [], []
        self.traverse(root1, r1)
        self.traverse(root2, r2)
        return r1 == r2

    def traverse(self, node, res):
        if node:
            if node.left is None and node.right is None:
                res.append(node.val)
            self.traverse(node.left, res)
            self.traverse(node.right, res)


def test_leaf_similar():
    a = TreeNode(1)
    b = TreeNode(3)
    c = TreeNode(2)
    d = TreeNode(5)
    a.left = b
    a.right = c
    c.left = d

    aa = TreeNode(6)
    bb = TreeNode(1)
    cc = TreeNode(2)
    dd = TreeNode(3)
    ee = TreeNode(5)
    aa.left = bb
    aa.right = cc
    bb.right = dd
    cc.right = ee

    assert Solution().leafSimilar(a, aa)
