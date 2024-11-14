class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
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
                    tmp= tmp.right

    def contains(self, value):
        if self.root is None:
            return False
        tmp = self.root

        while tmp is not None:
            if value == tmp.value:
                return True
            elif value < tmp.value:
                tmp = tmp.left
            elif value > tmp.value:
                tmp = tmp.right
        return False

    def bfs(self):
        queue = []
        result = []
        curr = self.root
        queue.append(curr) 
        if self.root is None:
            return result
        while queue:
            curr = queue.pop(0)
            result.append(curr.value)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)

        return result

    def dfs_preorder(self):
        pass

    def dfs_inorder(self):
        pass




bst = BST()
bst.insert(47)
bst.insert(21)
bst.insert(76)
bst.insert(18)
bst.insert(27)
bst.insert(52)
bst.insert(82)
# print(bst.root.value)
# print(bst.root.left.value)
# print(bst.root.right.value)
# print(bst.root.left.left.value)
print(bst.bfs())








































# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, value):
#         new_node = Node(value)
#         if self.root == None:
#             self.root = new_node
#             return True
#         tmp = self.root
#         while True:
#             if value == tmp.value:
#                 return False
#             if value < tmp.value:
#                 if tmp.left is None:
#                     tmp.left = new_node
#                     return True
#                 else:
#                     tmp = tmp.left
#             elif value > tmp.value:
#                 if tmp.right is None:
#                     tmp.right = new_node
#                     return True
#                 else:
#                     tmp = tmp.right
#
#     def bfs(self):
#         q = []
#         result = []
#         tmp = self.root
#         q.append(tmp)
#         while q:                            # i.e len(q) != 0:
#             curr = q.pop(0)                 # Remove from the front of the queue
#             if curr is not None:
#                 result.append(curr.value)
#             if curr.left is not None:
#                 q.append(curr.left)         # Add left child to the queue
#             if curr.right is not None:
#                 q.append(curr.right)        # Add right child to the queue
#         print(result)
#
#     def dfs_preorder(self):
#         def traverse(root: Node):
#             print(root.value)
#             if root.left is not None:
#                 traverse(root.left)
#             if root.right is not None:
#                 traverse(root.right)
#         traverse(self.root)
#
#     def dfs_inorder(self):
#         def traverse(current_value: Node):
#             if current_value.left is not None:
#                 traverse(current_value.left)
#             print(current_value.value)
#             if current_value.right is not None:
#                 traverse(current_value.right)
#         traverse(self.root)
#
#     def dfs_postorder(self):
#         def traverse(current_value: Node):
#             if current_value.left is not None:
#                 traverse(current_value.left)
#             if current_value.right is not None:
#                 traverse(current_value.right)
#             print(current_value.value)
#         traverse(self.root)
#
#
# bst = BinarySearchTree()
# bst.insert(47)
# bst.insert(21)
# bst.insert(76)
# bst.insert(18)
# bst.insert(27)
# bst.insert(52)
# bst.insert(82)
# print("   ", bst.root.value)
# print(" ", bst.root.left.value," ", bst.root.right.value)
# print(bst.root.left.left.value, bst.root.left.right.value,
#       bst.root.right.left.value, bst.root.right.right.value)
# bst.bfs()
# # bst.dfs_preorder()
# # bst.dfs_inorder()
# bst.dfs_postorder()