# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        stack1, stack2 = [], []
        self.traverse(root1, stack1)
        self.traverse(root2, stack2)
        return sorted(stack1 + stack2)

    def traverse(self, node, stack):
        if node:
            if node.left:
                self.traverse(node.left, stack)
            stack.append(node.val)
            if node.right:
                self.traverse(node.right, stack)


def test_get_all_elements_1():
    a = TreeNode(2)
    b = TreeNode(1)
    c = TreeNode(4)
    a.left = b
    a.right = c

    aa = TreeNode(1)
    bb = TreeNode(0)
    cc = TreeNode(3)
    aa.left = bb
    aa.right = cc

    s = Solution()
    assert [0, 1, 1, 2, 3, 4] == s.getAllElements(a, aa)


def test_get_all_elements_2():
    aa = TreeNode(5)
    bb = TreeNode(1)
    cc = TreeNode(7)
    dd = TreeNode(0)
    ee = TreeNode(2)
    aa.left = bb
    aa.right = cc
    bb.left = dd
    bb.right = ee

    s = Solution()
    assert [0, 1, 2, 5, 7] == s.getAllElements(None, aa)
