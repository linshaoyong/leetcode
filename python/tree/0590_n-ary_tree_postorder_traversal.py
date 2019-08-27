# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children)
        return res[::-1]


def test_post_order():
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

    assert [5, 6, 3, 2, 4, 1] == s.postorder(a)
