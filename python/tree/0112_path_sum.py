# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, summ):
        """
        :type root: TreeNode
        :type summ: int
        :rtype: bool
        """
        find = [False]
        self.traverse(root, [], summ, find)
        return find[0]

    def traverse(self, node, path, summ, find):
        if find[0]:
            return
        if node:
            path.append(node.val)
            if node.left is None and node.right is None:
                if sum(path) == summ:
                    find[0] = True
                path.pop()
                return
            self.traverse(node.left, path, summ, find)
            self.traverse(node.right, path, summ, find)
            path.pop()


def test_has_path_sum():
    a = TreeNode(5)
    b = TreeNode(4)
    c = TreeNode(8)
    d = TreeNode(11)
    e = TreeNode(13)
    f = TreeNode(4)
    g = TreeNode(7)
    h = TreeNode(2)
    i = TreeNode(1)
    a.left = b
    a.right = c
    b.left = d
    c.left = e
    c.right = f
    d.left = g
    d.right = h
    f.right = i
    assert Solution().hasPathSum(a, 18)
    assert Solution().hasPathSum(a, 22)
    assert Solution().hasPathSum(a, 26)
    assert Solution().hasPathSum(a, 27)
    assert Solution().hasPathSum(a, 19) is False
