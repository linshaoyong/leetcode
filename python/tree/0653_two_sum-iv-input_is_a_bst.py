# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        finded = [False]
        self.traverse(root, set(), k, finded)
        return finded[0]

    def traverse(self, node, targets, k, finded):
        if finded[0]:
            return
        if node:
            if node.val in targets:
                finded[0] = True
            else:
                targets.add(k - node.val)
                self.traverse(node.left, targets, k, finded)
                self.traverse(node.right, targets, k, finded)


def test_find_target():
    a = TreeNode(5)
    b = TreeNode(3)
    c = TreeNode(6)
    d = TreeNode(2)
    e = TreeNode(4)
    f = TreeNode(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    assert Solution().findTarget(a, 9)
    assert Solution().findTarget(a, 28) is False
