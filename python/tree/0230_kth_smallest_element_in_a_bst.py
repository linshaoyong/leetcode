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
        a = [root]
        b = []
        c = [root.val]
        while True:
            for n in a:
                if n.left:
                    b.append(n.left)
                    c.append(n.left.val)
                if n.right:
                    b.append(n.right)
                    c.append(n.right.val)
            if not b:
                break
            else:
                a = b
                b = []
        return sorted(c)[k - 1]


def test_0():
    a = TreeNode(3)
    b = TreeNode(1)
    c = TreeNode(4)
    d = TreeNode(2)

    a.left = b
    a.right = c
    b.right = d

    assert Solution().kthSmallest(a, 1) == 1
    assert Solution().kthSmallest(a, 2) == 2
    assert Solution().kthSmallest(a, 3) == 3
    assert Solution().kthSmallest(a, 4) == 4
