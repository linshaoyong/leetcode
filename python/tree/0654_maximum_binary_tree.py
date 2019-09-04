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
        if not nums:
            return None
        i, v = self.find_max(nums)
        node = TreeNode(v)
        self.traversal(node, nums[0:i], nums[i + 1:])
        return node

    def traversal(self, parent, lns, rns):
        if parent:
            if lns:
                i, v = self.find_max(lns)
                left = TreeNode(v)
                parent.left = left
                self.traversal(left, lns[0:i], lns[i + 1:])
            if rns:
                i, v = self.find_max(rns)
                right = TreeNode(v)
                parent.right = right
                self.traversal(right, rns[0:i], rns[i + 1:])

    def find_max(self, nums):
        if nums:
            m = (0, nums[0])
            for i in range(1, len(nums)):
                if nums[i] > m[1]:
                    m = (i, nums[i])
            return m
        return None


def test_construct_maximum_binary_tree():
    s = Solution()
    a = s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    assert 6 == a.val
    assert 3 == a.left.val
    assert 5 == a.right.val
    assert 2 == a.left.right.val
    assert 1 == a.left.right.right.val
    assert 0 == a.right.left.val
