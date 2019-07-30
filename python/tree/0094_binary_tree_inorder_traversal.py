class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        current = root
        s = []
        r = []
        done = 0
        while not done:
            if current is not None:
                s.append(current)
                current = current.left
            else:
                if len(s) > 0:
                    current = s.pop()
                    r.append(current.val)
                    current = current.right
                else:
                    done = 1
        return r


def test_in_order_traversal():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.right = b
    b.left = c

    assert Solution().inorderTraversal(a) == [1, 3, 2]
