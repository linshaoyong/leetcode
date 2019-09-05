# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        for n in preorder[1:]:
            self.insert(root, root, n)
        return root

    def insert(self, parent, node, n):
        if node is None:
            if n < parent.val:
                parent.left = TreeNode(n)
            else:
                parent.right = TreeNode(n)
            return
        if n < node.val:
            self.insert(node, node.left, n)
        else:
            self.insert(node, node.right, n)


def test_bst_from_preorder():
    root = Solution().bstFromPreorder([8, 5, 1, 7, 10, 12])
    assert 8 == root.val
    assert 5 == root.left.val
    assert 10 == root.right.val
    assert 1 == root.left.left.val
    assert 7 == root.left.right.val
    assert 12 == root.right.right.val
