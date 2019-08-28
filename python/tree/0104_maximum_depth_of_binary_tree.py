# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        a = [root]
        b = []
        d = 1
        while True:
            for n in a:
                if n.left:
                    b.append(n.left)
                if n.right:
                    b.append(n.right)
            if not b:
                break
            else:
                d += 1
                a = b
                b = []
        return d


def test_max_depth():
    assert Solution().maxDepth(None) == 0

    a = TreeNode(3)
    assert Solution().maxDepth(a) == 1

    b = TreeNode(9)
    c = TreeNode(20)
    a.left = b
    a.right = c
    d = TreeNode(15)
    e = TreeNode(7)
    c.left = d
    c.right = e
    assert Solution().maxDepth(a) == 3
