# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        nodes = []
        self.traverse(root, nodes)
        addition = 0
        for i in range(len(nodes) - 1, -1, -1):
            nodes[i].val += addition
            addition = nodes[i].val
        return root

    def traverse(self, node, nodes):
        if node:
            self.traverse(node.left, nodes)
            nodes.append(node)
            self.traverse(node.right, nodes)


def test_convert_bst():
    a = TreeNode(5)
    b = TreeNode(2)
    c = TreeNode(13)
    a.left = b
    a.right = c

    a = Solution().convertBST(a)
    assert 18 == a.val
    assert 20 == a.left.val
    assert 13 == a.right.val

    a = TreeNode(2)
    b = TreeNode(1)
    a.left = b

    a = Solution().convertBST(a)
    assert 2 == a.val
    assert 3 == a.left.val

    a = TreeNode(2)
    b = TreeNode(0)
    c = TreeNode(3)
    d = TreeNode(-4)
    e = TreeNode(1)
    a.left = b
    a.right = c
    b.left = d
    b.right = e

    a = Solution().convertBST(a)
    assert 5 == a.val
    assert 6 == a.left.val
    assert 3 == a.right.val
    assert 2 == a.left.left.val
    assert 6 == a.left.right.val
