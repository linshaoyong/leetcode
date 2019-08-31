# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        a = [root]
        r = []
        while a:
            b = []
            v = []
            for n in a:
                v.append(n.val)
                if n.left:
                    b.append(n.left)
                if n.right:
                    b.append(n.right)
            a = b
            b = []
            if v:
                r.append(max(v))
        return r


def test_largest_values():
    a = TreeNode(1)
    b = TreeNode(3)
    c = TreeNode(2)
    d = TreeNode(5)
    e = TreeNode(3)
    f = TreeNode(9)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    assert [1, 3, 9] == Solution().largestValues(a)
