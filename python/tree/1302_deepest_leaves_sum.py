# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a = [root]
        while a:
            b = []
            for n in a:
                if n.left:
                    b.append(n.left)
                if n.right:
                    b.append(n.right)
            if not b:
                break
            a = b
        return sum([n.val for n in a])


def test_deepest_leaves_sum():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c

    d = TreeNode(4)
    e = TreeNode(5)
    b.left = d
    b.right = e

    f = TreeNode(6)
    c.right = f

    g = TreeNode(7)
    d.left = g
    h = TreeNode(8)
    f.right = h

    s = Solution()
    assert 15 == s.deepestLeavesSum(a)
