class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.res, self.c, self.found = 0, 0, False
        self.find(root, k)
        return self.res

    def find(self, node, k):
        if not self.found and node:
            self.find(node.left, k)

            self.c += 1
            if self.c == k:
                self.res = node.val
                self.found = True
            self.find(node.right, k)


def test_0():
    a = TreeNode(3)
    b = TreeNode(1)
    c = TreeNode(4)
    d = TreeNode(2)

    a.left = b
    a.right = c
    b.right = d

    assert 1 == Solution().kthSmallest(a, 1)
    assert 2 == Solution().kthSmallest(a, 2)
    assert 3 == Solution().kthSmallest(a, 3)
    assert 4 == Solution().kthSmallest(a, 4)
