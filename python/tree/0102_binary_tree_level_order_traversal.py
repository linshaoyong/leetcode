# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        a = [root]
        b = []
        r = [[root.val]]
        while a:
            c = []
            for n in a:
                if n.left:
                    b.append(n.left)
                    c.append(n.left.val)
                if n.right:
                    b.append(n.right)
                    c.append(n.right.val)
            if c:
                r.append(c)
            a = b
            b = []
        return r


def test_level_order_1():
    assert Solution().levelOrder(None) == []


def test_level_order_2():
    a = TreeNode(3)
    assert Solution().levelOrder(a) == [[3]]


def test_level_order_3():
    a = TreeNode(1)
    b = TreeNode(1)
    a.left = b
    assert Solution().levelOrder(a) == [[1], [1]]


def test_level_order_4():
    a = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    a.left = b
    a.right = c
    assert Solution().levelOrder(a) == [[2], [1, 3]]


def test_level_order_5():
    a = TreeNode(5)
    b = TreeNode(1)
    c = TreeNode(7)
    a.left = b
    a.right = c
    d = TreeNode(3)
    e = TreeNode(8)
    c.left = d
    c.right = e
    assert Solution().levelOrder(a) == [[5], [1, 7], [3, 8]]


def test_level_order_6():
    a = TreeNode(5)
    b = TreeNode(3)
    c = TreeNode(9)
    a.left = b
    a.right = c

    d = TreeNode(1)
    e = TreeNode(4)
    b.left = d
    b.right = e

    f = TreeNode(6)
    g = TreeNode(10)
    c.left = f
    c.right = g
    assert Solution().levelOrder(a) == [[5], [3, 9], [1, 4, 6, 10]]
