# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """


def test_find_duplicate_subtrees_1():
    assert [] == Solution().findDuplicateSubtrees(None)


def test_find_duplicate_subtrees_2():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(2)
    f = TreeNode(4)
    g = TreeNode(4)

    a.left = b
    a.right = c
    b.left = d
    c.left = e
    c.right = f
    e.left = g

    r = Solution().findDuplicateSubtrees(a)
    assert 2 == len(r)
    assert r[0].val in [2, 4]
    assert r[1].val in [2, 4]
