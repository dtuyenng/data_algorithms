class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        tmp = self.root
        parent = None
        while True:
            if value < tmp.value:
                parent = tmp
                tmp = tmp.left
                if tmp is None:
                    parent.left = new_node
                    break
            elif value > tmp.value:
                parent = tmp
                tmp = tmp.right
                if tmp is None:
                    parent.right = new_node
                    break
            else:
                # print("equal")
                return False
        # print(f"tmp: {tmp}")
        return True

    def insert2(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True

        tmp = self.root
        while True:
            if value < tmp.value:
                if tmp.left is None:
                    tmp.left = new_node
                    return True
                else:
                    tmp = tmp.left
            elif value > tmp.value:
                if tmp.right is None:
                    tmp.right = new_node
                    return True
                else:
                    tmp = tmp.right
            else:
                return False



bst = BinarySearchTree()
bst.insert2(47)
bst.insert2(21)
bst.insert2(76)
bst.insert2(18)
bst.insert2(27)
bst.insert2(52)
bst.insert2(82)
print("   ", bst.root.value)
print(" ", bst.root.left.value," ", bst.root.right.value)
print(bst.root.left.left.value, bst.root.left.right.value,
      bst.root.right.left.value, bst.root.right.right.value)
