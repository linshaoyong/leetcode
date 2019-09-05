# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        self.traverse(root, [], paths)
        return paths

    def traverse(self, node, res, paths):
        if node:
            res.append(str(node.val))
            if node.left is None and node.right is None:
                paths.append('->'.join(res))
                res.pop()
                return
            self.traverse(node.left, res, paths)
            self.traverse(node.right, res, paths)
            res.pop()


def test_binary_tree_paths():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(5)
    a.left = b
    a.right = c
    b.right = d

    assert ["1->2->5", "1->3"] == Solution().binaryTreePaths(a)
