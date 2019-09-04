# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        a = [root]
        parent_nodes = {root.val: root}
        bottom = set()
        while a:
            b = []
            for n in a:
                if n.left:
                    b.append(n.left)
                    parent_nodes[n.left.val] = n
                if n.right:
                    b.append(n.right)
                    parent_nodes[n.right.val] = n
            if not b:
                bottom = set(a)
            a = b

        while len(bottom) > 1:
            bottom = {parent_nodes[node.val] for node in bottom}
        return bottom.pop()


def test_subtree_with_all_deepest_1():
    a = TreeNode(1)

    node = Solution().subtreeWithAllDeepest(a)
    assert 1 == node.val


def test_subtree_with_all_deepest_2():
    a = TreeNode(3)
    b = TreeNode(5)
    c = TreeNode(1)
    d = TreeNode(6)
    e = TreeNode(2)
    f = TreeNode(0)
    g = TreeNode(8)
    h = TreeNode(7)
    i = TreeNode(4)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.left = h
    e.right = i

    node = Solution().subtreeWithAllDeepest(a)
    assert 2 == node.val
    assert 7 == node.left.val
    assert 4 == node.right.val


def test_subtree_with_all_deepest_3():
    a = TreeNode(0)
    b = TreeNode(1)
    c = TreeNode(3)
    d = TreeNode(2)
    a.left = b
    a.right = c
    b.right = d

    node = Solution().subtreeWithAllDeepest(a)
    assert 2 == node.val


def test_subtree_with_all_deepest_4():
    a = TreeNode(0)
    b = TreeNode(1)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(7)
    f = TreeNode(4)
    g = TreeNode(5)
    h = TreeNode(6)
    i = TreeNode(8)
    j = TreeNode(9)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h
    d.right = i
    e.right = j

    node = Solution().subtreeWithAllDeepest(a)
    assert 1 == node.val
    assert 3 == node.left.val
    assert 7 == node.right.val
    assert 6 == node.left.left.val
    assert 8 == node.left.right.val
    assert 9 == node.right.right.val
