# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """


def test_construct_maximum_binary_tree():
    s = Solution()
    a = s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    assert 6 == a.val
    assert 3 == a.left.val
    assert 5 == a.right.val
    assert 2 == a.left.right.val
    assert 1 == a.left.right.right.val
    assert 0 == a.right.left.val
