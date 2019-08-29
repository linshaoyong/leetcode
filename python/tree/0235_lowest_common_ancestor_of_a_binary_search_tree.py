# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pp, qq = min(p, q), max(p, q)
        return self.find(root, pp, qq)

    def find(self, node, pp, qq):
        if node:
            if node.val >= pp and node.val <= qq:
                return node
            if node.val > qq:
                return self.find(node.left, pp, qq)
            if node.val < pp:
                return self.find(node.right, pp, qq)


def test_lowest_common_ancestor():
    a = TreeNode(6)
    b = TreeNode(2)
    c = TreeNode(8)
    d = TreeNode(0)
    e = TreeNode(4)
    f = TreeNode(7)
    g = TreeNode(9)
    h = TreeNode(3)
    i = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.left = h
    e.right = i
    assert 6 == Solution().lowestCommonAncestor(a, 2, 8).val
    assert 2 == Solution().lowestCommonAncestor(a, 2, 4).val
