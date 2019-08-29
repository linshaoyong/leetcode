# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        res = []
        self.traversal(root, res)
        if len(res) == 1:
            return abs(res[0])
        minv = abs(res[1].val - res[0].val)
        prev = res[0]
        for n in res[1:]:
            minv = min(minv, abs(n.val - prev.val))
            prev = n
        return minv

    def traversal(self, node, res):
        if node:
            self.traversal(node.left, res)
            res.append(node)
            self.traversal(node.right, res)


def test_min_diff_in_bst():
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(6)
    d = TreeNode(1)
    e = TreeNode(3)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    assert 1 == Solution().minDiffInBST(a)
