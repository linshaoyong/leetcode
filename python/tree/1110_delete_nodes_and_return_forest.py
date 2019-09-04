# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        if not root:
            return []
        tds = set(to_delete)
        nodes = [(None, False, root,)]
        res = []
        if root.val not in tds:
            res.append(root)
        while nodes:
            parent, is_left, curr = nodes.pop()
            if curr.left:
                nodes.append((curr, True, curr.left,))
                if curr.val in tds and curr.left.val not in tds:
                    res.append(curr.left)
            if curr.right:
                nodes.append((curr, False, curr.right,))
                if curr.val in tds and curr.right.val not in tds:
                    res.append(curr.right)
            if parent and curr.val in tds:
                if is_left:
                    parent.left = None
                else:
                    parent.right = None
        return res


def test_del_nodes_1():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    roots = Solution().delNodes(a, [3, 5])
    assert 3 == len(roots)
    rvs = [r.val for r in roots]
    assert 1 in rvs
    assert 6 in rvs
    assert 7 in rvs


def test_del_nodes_2():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(4)
    d = TreeNode(3)
    a.left = b
    b.left = c
    b.right = d

    roots = Solution().delNodes(a, [2, 3])
    assert 2 == len(roots)
    rvs = [r.val for r in roots]
    assert 1 in rvs
    assert 4 in rvs
