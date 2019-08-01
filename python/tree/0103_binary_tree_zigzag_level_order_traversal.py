class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        a = [root]
        b = []
        c = []
        r = [[root.val]]
        i = 1
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
                if i & 1 == 1:
                    c.reverse()
                r.append(c)
                b = []
                c = []
                i += 1
        return r


def test_zigzag_level_order():
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.left = b
    a.right = c
    c.left = d
    c.right = e

    assert Solution().zigzagLevelOrder(a) == [
        [3],
        [20, 9],
        [15, 7]
    ]
