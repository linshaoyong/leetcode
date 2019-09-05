# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        values = [0]
        self.traverse(root, [], values)
        return values[0]

    def traverse(self, node, res, values):
        if node:
            res.append(node.val)
            if node.left is None and node.right is None:
                values[0] = values[0] + self.leafValue(res)
                res.pop()
                return
            self.traverse(node.left, res, values)
            self.traverse(node.right, res, values)
            res.pop()

    def leafValue(self, res):
        s = 0
        for i, v in enumerate(res[::-1]):
            s += v * pow(2, i)
        return s


def test_sum_root_to_leaf():
    a = TreeNode(1)
    b = TreeNode(0)
    c = TreeNode(1)
    d = TreeNode(0)
    e = TreeNode(1)
    f = TreeNode(0)
    g = TreeNode(1)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    assert 22 == Solution().sumRootToLeaf(a)
