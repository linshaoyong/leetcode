# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
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
            r.append(a[-1].val)
            for n in a:
                if n.left:
                    b.append(n.left)
                if n.right:
                    b.append(n.right)
            a = b
            b = []
        return r


def test_right_side_view():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(5)
    e = TreeNode(4)
    a.left = b
    a.right = c
    b.right = d
    c.right = e
    assert [1, 3, 4] == Solution().rightSideView(a)
