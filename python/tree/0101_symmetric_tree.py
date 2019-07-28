# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        a = [root]
        b = []
        while True:
            for n in a:
                if n is None:
                    continue
                b.append(n.left)
                b.append(n.right)
            if not b:
                break
            else:
                a = b
                if not self.isSymmetricArray(a):
                    return False
                b = []
        return True

    def isSymmetricArray(self, arr):
        length = len(arr)
        for i in range(0, length // 2):
            if arr[i] is None and arr[length - i - 1] is None:
                continue
            if arr[i] is None:
                return False
            if arr[length - i - 1] is None:
                return False
            if arr[i].val != arr[length - i - 1].val:
                return False
        return True


def test_is_symmetric_1():
    a = TreeNode(1)
    assert Solution().isSymmetric(a) is True


def test_is_symmetric_2():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    a.left = b
    a.right = c
    assert Solution().isSymmetric(a) is True


def test_is_symmetric_3():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(4)
    g = TreeNode(3)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    assert Solution().isSymmetric(a) is True


def test_is_symmetric_4():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(3)
    a.left = b
    a.right = c
    b.right = d
    c.right = e
    assert Solution().isSymmetric(a) is False


def test_is_symmetric_5():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(3)
    a.left = b
    a.right = c
    b.right = d
    c.left = e
    assert Solution().isSymmetric(a) is True


def test_is_symmetric_6():
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(5)
    g = TreeNode(4)
    h = TreeNode(8)
    i = TreeNode(9)
    j = TreeNode(9)
    k = TreeNode(8)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.left = h
    e.right = i
    g.left = j
    g.right = k
    assert Solution().isSymmetric(a) is False
