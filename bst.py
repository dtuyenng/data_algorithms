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
            if value == tmp.value:
                return False
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

    def bfs(self):
        q = []
        result = []

        tmp = self.root
        q.append(tmp)
        while q:                            # i.e len(q) != 0:
            curr = q.pop(0)                 # Remove from the front of the queue
            if curr is not None:
                result.append(curr.value)
            if curr.left is not None:
                q.append(curr.left)         # Add left child to the queue
            if curr.right is not None:
                q.append(curr.right)        # Add right child to the queue
        print(result)

    def dfs_preorder(self):
        def traverse(root: Node):
            print(root.value)
            if root.left is not None:
                traverse(root.left)
            if root.right is not None:
                traverse(root.right)
        traverse(self.root)

    def dfs_inorder(self):
        def traverse(current_value: Node):
            if current_value.left is not None:
                traverse(current_value.left)
            print(current_value.value)
            if current_value.right is not None:
                traverse(current_value.right)
        traverse(self.root)

    def dfs_postorder(self):
        def traverse(current_value: Node):
            if current_value.left is not None:
                traverse(current_value.left)
            if current_value.right is not None:
                traverse(current_value.right)
            print(current_value.value)
        traverse(self.root)


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
bst.bfs()
# bst.dfs_preorder()
# bst.dfs_inorder()
bst.dfs_postorder()