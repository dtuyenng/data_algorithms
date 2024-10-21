class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        new_node = Node(8)
        self.root = new_node

    def insert(self, value):
        pass

bst = BinarySearchTree()
print(bst.root.left)