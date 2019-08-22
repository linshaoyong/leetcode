# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        f, s = self.find(root, root.val, root.val)
        if f == s:
            return -1
        return s

    def find(self, node, first, second):
        f = first
        s = second
        if node:
            if first == second:
                if node.val > second:
                    s = node.val
            else:
                if node.val < first:
                    s = f
                    f = node.val
                elif node.val > first and node.val < second:
                    s = node.val
            f, s = self.find(node.left, f, s)
            f, s = self.find(node.right, f, s)
        return f, s


def test_find_second_minimum_value():
    s = Solution()

    a = TreeNode(2)
    b = TreeNode(2)
    c = TreeNode(5)
    d = TreeNode(5)
    e = TreeNode(7)
    a.left = b
    a.right = c
    c.left = d
    c.right = e
    assert 5 == s.findSecondMinimumValue(a)

    a = TreeNode(2)
    b = TreeNode(2)
    c = TreeNode(2)
    a.left = b
    a.right = c
    assert -1 == s.findSecondMinimumValue(a)
