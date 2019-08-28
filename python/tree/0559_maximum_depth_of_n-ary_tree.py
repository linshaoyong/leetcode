# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        a = [root]
        b = []
        depth = 1
        while True:
            for n in a:
                if n.children:
                    b.extend(n.children)
            if not b:
                break
            else:
                a = b
                b = []
                depth += 1
        return depth


def test_max_depth():
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

    assert 3 == Solution().maxDepth(a)
