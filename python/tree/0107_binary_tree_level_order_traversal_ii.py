# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        a = [root]
        b = []
        r = []
        while a:
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
                r.append(v)
        return r[::-1]


def test_level_order_bottom():
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.left = b
    a.right = c
    c.left = d
    c.right = e

    assert [
        [15, 7],
        [9, 20],
        [3]
    ] == Solution().levelOrderBottom(a)
