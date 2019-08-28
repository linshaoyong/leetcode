# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root):
        res = []
        self.traversal(root, res)
        return res

    def traversal(self, node, res):
        if node:
            res.append(node.val)
            for child in node.children:
                self.traversal(child, res)


def test_preorder():
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

    assert [1, 3, 5, 6, 2, 4] == Solution().preorder(a)
