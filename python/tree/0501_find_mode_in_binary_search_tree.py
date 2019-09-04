# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        m = {}
        self.traversal(root, m)
        res = []
        maxv = 0
        for k, v in sorted(m.items(), key=lambda kv: kv[1], reverse=True):
            if maxv == 0:
                maxv = v
                res.append(k)
                continue
            if maxv == v:
                res.append(k)
                continue
            break
        return res

    def traversal(self, node, m):
        if node:
            m[node.val] = m.get(node.val, 0) + 1
            self.traversal(node.left, m)
            self.traversal(node.right, m)
        return m


def test_find_mode():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    a.right = b
    b.left = c
    assert [2] == Solution().findMode(a)
