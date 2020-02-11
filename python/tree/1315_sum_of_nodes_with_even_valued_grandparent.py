# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.traverse(root, None, None, res)
        return res[0]

    def traverse(self, node, pnode, gpnode, sum_even):
        if node:
            if gpnode and gpnode.val % 2 == 0:
                sum_even[0] += node.val
            if node.left:
                self.traverse(node.left, node, pnode, sum_even)
            if node.right:
                self.traverse(node.right, node, pnode, sum_even)


def test_sum_even_grand_parent():
    a = TreeNode(6)
    b = TreeNode(7)
    c = TreeNode(8)
    a.left = b
    a.right = c

    d = TreeNode(2)
    e = TreeNode(7)
    b.left = d
    b.right = e

    f = TreeNode(1)
    h = TreeNode(3)
    c.left = f
    c.right = h

    i = TreeNode(9)
    j = TreeNode(1)
    k = TreeNode(4)
    m = TreeNode(5)
    d.left = i
    e.left = j
    e.right = k
    h.right = m

    s = Solution()
    assert 18 == s.sumEvenGrandparent(a)
