# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        res = [str(t.val)]
        if t.left is None and t.right:
            res[0] += '()'
        self.traverse(t.left, res)
        self.traverse(t.right, res)
        return res[0]

    def traverse(self, node, res):
        if node:
            res[0] += '(' + str(node.val)
            if node.left:
                self.traverse(node.left, res)
            else:
                if node.right:
                    res[0] += '()'
            if node.right:
                self.traverse(node.right, res)
            res[0] += ')'


def test_tree2str():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    a.left = b
    a.right = c
    b.left = d

    assert "1(2(4))(3)" == Solution().tree2str(a)

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    a.left = b
    a.right = c
    b.right = d
    assert "1(2()(4))(3)" == Solution().tree2str(a)

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    a.right = b
    b.right = c
    c.right = d
    d.right = e
    e.right = f
    assert "1()(2()(3()(4()(5()(6)))))" == Solution().tree2str(a)
