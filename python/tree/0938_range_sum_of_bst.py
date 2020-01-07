class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        a = [root]
        c = 0
        while a:
            b = []
            for n in a:
                if n.val >= L and n.val <= R:
                    c += n.val
                if n.left:
                    b.append(n.left)
                if n.right:
                    b.append(n.right)
            a = b
        return c


def test_range_sum_bst_1():
    s = Solution()

    root = TreeNode(10)
    n1 = TreeNode(5)
    n2 = TreeNode(15)
    root.left = n1
    root.right = n2

    n3 = TreeNode(3)
    n4 = TreeNode(7)
    n1.left = n3
    n1.right = n4

    n5 = TreeNode(18)
    n2.right = n5
    assert 32 == s.rangeSumBST(root, 7, 15)


def test_range_sum_bst_2():
    s = Solution()

    root = TreeNode(15)
    n1 = TreeNode(9)
    n2 = TreeNode(21)
    root.left = n1
    root.right = n2

    n3 = TreeNode(7)
    n4 = TreeNode(13)
    n1.left = n3
    n1.right = n4

    n5 = TreeNode(19)
    n6 = TreeNode(23)
    n2.left = n5
    n2.right = n6

    n7 = TreeNode(5)
    n3.left = n7

    n8 = TreeNode(11)
    n4.left = n8

    n9 = TreeNode(17)
    n5.left = n9
    assert 40 == s.rangeSumBST(root, 19, 21)
