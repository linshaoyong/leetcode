# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node = root
        while node:
            if node.val > val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
            if node.val < val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
        return root


def test_insert_into_bst():
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(7)
    d = TreeNode(1)
    e = TreeNode(3)
    a.left = b
    a.right = c
    b.left = d
    b.right = e

    a = Solution().insertIntoBST(a, 5)
    assert 4 == a.val
    assert 2 == a.left.val
    assert 7 == a.right.val
    assert 1 == a.left.left.val
    assert 3 == a.left.right.val
    assert 5 == a.right.left.val
