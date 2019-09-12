# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = [(root, True,)]
        while stack:
            node, fresh = stack.pop()
            if not fresh:
                res.append(node.val)
                continue
            stack.append((node, False,))
            if node.right:
                stack.append((node.right, True,))
            if node.left:
                stack.append((node.left, True,))

            if node.left is None and node.right is None:
                node, _ = stack.pop()
                res.append(node.val)
        return res


def test_postorder_traversal():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.right = b
    b.left = c

    assert [3, 2, 1] == Solution().postorderTraversal(a)
