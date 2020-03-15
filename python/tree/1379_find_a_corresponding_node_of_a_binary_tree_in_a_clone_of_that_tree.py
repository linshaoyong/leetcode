import copy

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        self.res = None
        self.traverse(original, cloned, target)
        return self.res

    def traverse(self, node, nodec, target):
        if node:
            if node == target:
                self.res = nodec
                return
            if node.left:
                self.traverse(node.left, nodec.left, target)
            if node.right:
                self.traverse(node.right, nodec.right, target)


def test_get_target_copy_1():
    s = Solution()

    a = TreeNode(7)
    b = TreeNode(4)
    c = TreeNode(3)
    d = TreeNode(6)
    e = TreeNode(19)

    a.left = b
    a.right = c
    c.left = d
    c.right = e

    aa = copy.deepcopy(a)
    cc = s.getTargetCopy(a, aa, c)
    assert 3 == cc.val
    assert 6 == cc.left.val
    assert 19 == cc.right.val


def test_get_target_copy_2():
    s = Solution()

    a = TreeNode(7)
    aa = copy.deepcopy(a)

    aaa = s.getTargetCopy(a, aa, a)
    assert 7 == aaa.val
