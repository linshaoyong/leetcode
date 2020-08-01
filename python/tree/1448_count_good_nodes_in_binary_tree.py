# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = [0]
        self.traverse(root, root.val, ret)
        return ret[0]

    def traverse(self, node, current_max, ret):
        if node:
            if node.val >= current_max:
                ret[0] += 1
                current_max = node.val
            self.traverse(node.left, current_max, ret)
            self.traverse(node.right, current_max, ret)


def test_good_nodes_1():
    s = Solution()

    a = TreeNode(3)
    b = TreeNode(1)
    c = TreeNode(4)
    d = TreeNode(3)
    e = TreeNode(1)
    f = TreeNode(5)

    a.left = b
    a.right = c

    b.left = d
    c.left = e
    c.right = f

    assert 4 == s.goodNodes(a)


def test_good_nodes_2():
    s = Solution()

    a = TreeNode(9)
    b = TreeNode(3)
    c = TreeNode(6)

    a.right = b
    b.right = c

    assert 1 == s.goodNodes(a)
