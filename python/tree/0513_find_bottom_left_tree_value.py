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
        a = [(root, False,)]
        leftv = root.val
        while a:
            b = []
            first = True
            for n, is_left in a:
                if first and is_left:
                    leftv = n.val
                    first = False
                if n.left:
                    b.append((n.left, True,))
                if n.right:
                    b.append((n.right, False,))
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
