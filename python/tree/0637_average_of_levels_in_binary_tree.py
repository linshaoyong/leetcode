# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return []
        a = [root]
        b = []
        r = []
        while a:
            s, c = 0, 0
            for n in a:
                s += n.val
                c += 1
                if n.left:
                    b.append(n.left)
                if n.right:
                    b.append(n.right)
            r.append(float(s) / c)
            a = b
            b = []
        return r


def test_average_of_levels():
    s = Solution()

    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.left = b
    a.right = c
    c.left = d
    c.right = e

    assert [3, 14.5, 11] == s.averageOfLevels(a)
