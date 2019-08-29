# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        a = [root]
        b = []
        c = []
        while a:
            v = {}
            for n in a:
                if n.left:
                    b.append(n.left)
                    v[n.left.val] = n.val
                if n.right:
                    b.append(n.right)
                    v[n.right.val] = n.val
            if v:
                c.append(v)
            a = b
            b = []
        for d in c:
            if x in d and y in d and d[x] != d[y]:
                return True
        return False


def test_is_cousins():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    a.left = b
    a.right = c
    b.left = d
    assert Solution().isCousins(a, 3, 4) is False

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    b.right = d
    c.right = e
    assert Solution().isCousins(a, 5, 4)

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    a.left = b
    a.right = c
    b.right = d
    assert Solution().isCousins(a, 2, 3) is False
