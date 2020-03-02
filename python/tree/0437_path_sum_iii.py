# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, _sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.paths = 0
        self.dfs(root, _sum)
        return self.paths

    def dfs(self, node, target):
        if node:
            self.find_path(node, target)
            self.dfs(node.left, target)
            self.dfs(node.right, target)

    def find_path(self, node, target):
        if not node:
            return

        if node.val == target:
            self.paths += 1
        self.find_path(node.left, target - node.val)
        self.find_path(node.right, target - node.val)


def test_path_sum():
    a = TreeNode(10)
    b = TreeNode(5)
    c = TreeNode(-3)
    a.left = b
    a.right = c

    d = TreeNode(3)
    e = TreeNode(2)
    f = TreeNode(11)
    b.left = d
    b.right = e
    c.right = f

    h = TreeNode(3)
    i = TreeNode(-2)
    j = TreeNode(1)
    d.left = h
    d.right = i
    e.right = j

    s = Solution()
    assert 3 == s.pathSum(a, 8)
