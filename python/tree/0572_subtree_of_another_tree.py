# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        nodes = []
        self.find(s, t.val, nodes)
        if not nodes:
            return False
        for node in nodes:
            if self.same_tree(node, t):
                return True
        return False

    def find(self, node, value, nodes):
        if node:
            if node.val == value:
                nodes.append(node)
            self.find(node.left, value, nodes)
            self.find(node.right, value, nodes)

    def same_tree(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val != t.val:
            return False
        if self.same_tree(s.left, t.left) and self.same_tree(s.right, t.right):
            return True
        return False


def test_is_subtree():
    a = TreeNode(3)
    b = TreeNode(4)
    c = TreeNode(5)
    d = TreeNode(1)
    e = TreeNode(2)
    a.left = b
    a.right = c
    b.left = d
    b.right = e

    o = TreeNode(4)
    p = TreeNode(1)
    q = TreeNode(2)
    o.left = p
    o.right = q
    assert Solution().isSubtree(a, o)

    f = TreeNode(0)
    e.left = f
    assert Solution().isSubtree(a, o) is False

    a = TreeNode(1)
    b = TreeNode(1)
    a.left = b

    o = TreeNode(1)
    assert Solution().isSubtree(a, o)
