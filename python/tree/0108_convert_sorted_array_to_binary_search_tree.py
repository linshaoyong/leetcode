# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


def test_sorted_array_to_BST():
    assert Solution().sortedArrayToBST(None) is None
    assert Solution().sortedArrayToBST([]) is None

    a = Solution().sortedArrayToBST([1])
    assert a.val == 1
    assert a.left is None
    assert a.right is None
