# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a = [root]
        level = 0
        maxl, maxv = 1, root.val
        while a:
            level += 1
            s = 0
            b = []
            for n in a:
                if n.left:
                    b.append(n.left)
                if n.right:
                    b.append(n.right)
                s += n.val
            a = b
            if s > maxv:
                maxl = level
                maxv = s
        return maxl


def test_max_level_sum():
    a = TreeNode(1)
    b = TreeNode(7)
    c = TreeNode(0)
    d = TreeNode(7)
    e = TreeNode(-8)
    a.left = b
    a.right = c
    b.left = d
    b.right = e

    assert 2 == Solution().maxLevelSum(a)
