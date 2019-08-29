# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getMinimumDifference(self, root):
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


def test_get_mininum_difference():
    a = TreeNode(1)
    b = TreeNode(3)
    c = TreeNode(2)
    a.right = b
    b.left = c
    assert 1 == Solution().getMinimumDifference(a)

    a = TreeNode(1)
    b = TreeNode(5)
    c = TreeNode(3)
    a.right = b
    b.left = c
    assert 2 == Solution().getMinimumDifference(a)

    a = TreeNode(1)
    b = TreeNode(2)
    a.right = b
    assert 1 == Solution().getMinimumDifference(a)

    a = TreeNode(236)
    b = TreeNode(104)
    c = TreeNode(701)
    d = TreeNode(227)
    e = TreeNode(911)
    a.left = b
    a.right = c
    b.right = d
    c.right = e
    assert 9 == Solution().getMinimumDifference(a)
