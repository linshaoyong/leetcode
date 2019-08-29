# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        nodes = [root]
        r = 0
        while nodes:
            node = nodes.pop()
            r = max(r, self.maxDepth(node.left) + self.maxDepth(node.right))
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return r

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        a = [root]
        b = []
        d = 0
        while a:
            for n in a:
                if n.left:
                    b.append(n.left)
                if n.right:
                    b.append(n.right)
            d += 1
            a = b
            b = []
        return d


def test_diameter_of_binary_tree():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    assert 3 == Solution().diameterOfBinaryTree(a)
