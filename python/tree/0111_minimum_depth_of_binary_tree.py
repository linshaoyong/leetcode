# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        a = [root]
        depth = 0
        while a:
            depth += 1
            b = []
            for n in a:
                if n.left is None and n.right is None:
                    return depth
                if n.left:
                    b.append(n.left)
                if n.right:
                    b.append(n.right)
            a = b
            b = []
        return depth


def test_min_depth():
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.left = b
    a.right = c
    c.left = d
    c.right = e

    assert 2 == Solution().minDepth(a)

    a = TreeNode(3)
    b = TreeNode(9)
    a.left = b
    assert 2 == Solution().minDepth(a)

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    c.right = e
    assert 3 == Solution().minDepth(a)

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    b.left = c
    c.left = d
    d.left = e
    assert 5 == Solution().minDepth(a)
