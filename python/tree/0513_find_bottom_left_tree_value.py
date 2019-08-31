# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return []
        a = [(root)]
        leftv = root.val
        while a:
            b = []
            leftv = a[0].val
            for n in a:
                if n.left:
                    b.append(n.left)
                if n.right:
                    b.append(n.right)
            a = b
            b = []
        return leftv


def test_find_bottom_left_value():
    a = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    a.left = b
    a.right = c
    assert 1 == Solution().findBottomLeftValue(a)

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    a.left = b
    a.right = c
    b.left = d
    c.left = e
    c.right = f
    e.left = g
    assert 7 == Solution().findBottomLeftValue(a)
