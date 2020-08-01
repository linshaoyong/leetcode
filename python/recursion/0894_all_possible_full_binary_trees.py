# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N < 3:
            return []


def test_all_possible_FBT():
    s = Solution()

    res = s.allPossibleFBT(7)
    assert 5 == len(res)
