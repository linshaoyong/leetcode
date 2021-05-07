class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self, value):
        self.root = TreeNode(value)

    def insert(self, value):
        self.binary_insert(value, self.root)

    def binary_insert(self, value, parent):
        if value < parent.val:
            if parent.left is None:
                parent.left = TreeNode(value)
            else:
                self.binary_insert(value, parent.left)
        else:
            if parent.right is None:
                parent.right = TreeNode(value)
            else:
                self.binary_insert(value, parent.right)

    def search(self, value):
        return self.binary_search(value, self.root)

    def binary_search(self, value, node):
        if node is None or node.val == value:
            return node
        if value > node.val:
            return self.binary_search(value, node.right)
        else:
            return self.binary_search(value, node.left)

    def delete(self, value):
        return self.binary_delete(value, self.root)

    def binary_delete(self, value, node):
        if node is None:
            return None
        elif value < node.val:
            node.left = self.binary_delete(value, node.left)
            return node
        elif value > node.val:
            node.right = self.binary_delete(value, node.right)
            return node
        elif value == node.val:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.right = self.lift(node.right, node)
                return node

    def lift(self, node, nodeToDelete):
        if node.left:
            node.left = self.lift(node.left, nodeToDelete)
            return node
        else:
            nodeToDelete.value = node.val
            return node.right


def test_tree_insert():
    tree = BinarySearchTree(4)
    tree.insert(2)
    tree.insert(7)
    tree.insert(1)
    tree.insert(3)

    root = tree.root
    assert 4 == root.val
    assert 2 == root.left.val
    assert 7 == root.right.val
    assert 1 == root.left.left.val
    assert 3 == root.left.right.val


def test_tree_search():
    tree = BinarySearchTree(4)
    tree.insert(2)
    tree.insert(7)
    tree.insert(1)
    tree.insert(3)

    found = tree.search(2)
    assert 2 == found.val
    assert 1 == found.left.val
    assert 3 == found.right.val
    assert found.left.left is None
    assert found.left.right is None
    assert found.right.left is None
    assert found.right.right is None

    assert tree.search(8) is None


def test_tree_delete():
    tree = BinarySearchTree(4)
    tree.insert(2)
    tree.insert(7)
    tree.insert(1)
    tree.insert(3)

    tree.delete(7)

    root = tree.root
    assert root.right is None

    tree.delete(1)
    assert 2 == root.left.val
    assert 3 == root.left.right.val
    assert root.left.left is None
