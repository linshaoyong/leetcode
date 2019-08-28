# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        a = [root]
        b = []
        r = []
        while a:
            v = []
            for n in a:
                v.append(n.val)
                for c in n.children:
                    b.append(c)
            r.append(v)
            a = b
            b = []
        return r


def test_level_order():
    s = Solution()
    a = Node(1, [])
    b = Node(3, [])
    c = Node(2, [])
    d = Node(4, [])
    e = Node(5, [])
    f = Node(6, [])
    a.children.append(b)
    a.children.append(c)
    a.children.append(d)
    b.children.append(e)
    b.children.append(f)

    assert [
        [1],
        [3, 2, 4],
        [5, 6]
    ] == s.levelOrder(a)
