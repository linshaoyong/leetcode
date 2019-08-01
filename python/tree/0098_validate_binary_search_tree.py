# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = []
        pre = None
        while root is not None or len(stack) > 0:
            while root is not None:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if pre is not None and root.val <= pre.val:
                return False
            pre = root
            root = root.right
        return True


def test_is_valid_bst_1():
    assert Solution().isValidBST(None) is True


def test_is_valid_bst_2():
    a = TreeNode(3)
    assert Solution().isValidBST(a) is True


def test_is_valid_bst_3():
    a = TreeNode(1)
    b = TreeNode(1)
    a.left = b
    assert Solution().isValidBST(a) is False


def test_is_valid_bst_4():
    a = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(3)
    a.left = b
    a.right = c
    assert Solution().isValidBST(a) is True


def test_is_valid_bst_5():
    a = TreeNode(5)
    b = TreeNode(1)
    c = TreeNode(7)
    a.left = b
    a.right = c
    d = TreeNode(3)
    e = TreeNode(8)
    c.left = d
    c.right = e
    assert Solution().isValidBST(a) is False


def test_is_valid_bst_6():
    a = TreeNode(5)
    b = TreeNode(3)
    c = TreeNode(9)
    a.left = b
    a.right = c

    d = TreeNode(1)
    e = TreeNode(4)
    b.left = d
    b.right = e

    f = TreeNode(6)
    g = TreeNode(10)
    c.left = f
    c.right = g
    assert Solution().isValidBST(a) is True
