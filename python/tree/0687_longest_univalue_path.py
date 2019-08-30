# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [root]
        maxp = 0
        while stack:
            node = stack.pop()
            maxp = max(maxp, self.univaluePath(node))
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return maxp

    def univaluePath(self, node):
        p = 0
        q = 0
        if node:
            if node.left:
                if node.val == node.left.val:
                    p += 1 + self.univaluePath(node.left)
            if node.right:
                if node.val == node.right.val:
                    q += 1 + self.univaluePath(node.right)
        return max(p, q)


def test_longest_univalue_path():
    a = TreeNode(5)
    b = TreeNode(4)
    c = TreeNode(5)
    d = TreeNode(1)
    e = TreeNode(1)
    f = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    assert 2 == Solution().longestUnivaluePath(a)

    a = TreeNode(1)
    b = TreeNode(4)
    c = TreeNode(5)
    d = TreeNode(4)
    e = TreeNode(4)
    f = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    assert 2 == Solution().longestUnivaluePath(a)

    a = TreeNode(1)
    b = TreeNode(1)
    c = TreeNode(1)
    d = TreeNode(1)
    e = TreeNode(1)
    f = TreeNode(1)
    g = TreeNode(1)
    a.right = b
    b.left = c
    b.right = d
    c.left = e
    c.right = f
    e.left = g
    assert 4 == Solution().longestUnivaluePath(a)
