# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None or root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        if root.val < val:
            return self.searchBST(root.right, val)


def test_search_bst():
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(7)
    d = TreeNode(1)
    e = TreeNode(3)
    a.left = b
    a.right = c
    b.left = d
    b.right = e

    root = Solution().searchBST(a, 2)
    assert 2 == root.val
    assert 1 == root.left.val
    assert 3 == root.right.val
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.left is None
    assert root.right.right is None
