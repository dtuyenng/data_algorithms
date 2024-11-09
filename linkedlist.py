



# from typing import Union
# """
# Linked List
#
# Methods:
#     print()
#     append(value)
#     prepend(value)
#     pop_first(value)
#     pop_last(value)
#     get(index)
#     set_value(value, index)
#     insert_value(value, index) *done*
#     remove_value(value, index)
#
#
# """
# from operator import truediv
#
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.pointer = None
#
#
# class LinkedList:
#     def __init__(self, value):
#         self.new_node = Node(value)
#         self.head = self.new_node
#         self.tail = self.new_node
#
#
#         self.length = 1
#
#     def print(self):
#         temp_node = self.head
#         print("Print")
#         while temp_node is not None:
#             print(f"{temp_node.value} -> ")
#             temp_node = temp_node.pointer
#
#     """
#         1. Create a new node,
#         2. Last node (currently tail) points to new node
#         3. Tail points to it (new location of tail
#         Time Complexity: O(1)
#     """
#
#     def append(self, value):
#         node = Node(value)
#         if self.head and self.tail is None:
#             self.head =  node
#             self.tail = node
#         else:
#             self.tail.pointer = node
#             self.tail = node
#             self.length += 1
#
#     """
#         1. Create new node
#         2. Set new node point to head
#         3. Set head to new node
#         Time Complexity: O(1)
#
#     """
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             self.length += 1
#         else:
#             new_node.pointer = self.head
#             self.head = new_node
#             self.length += 1
#
#
#     """
#         1. set node to be removed to head
#         2. set head to removed node's pointer
#         Time Complexity: 0(1)
#     """
#
#     def pop_first(self):
#
#         if self.length == 1:
#             removed_node = self.head
#             self.head = None
#             self.tail = None
#             self.length -= 1
#             return removed_node
#         elif self.length == 0:
#             return None
#         else:
#             removed_node = self.head
#             self.head = removed_node.pointer # or self.head = self.head.pointer
#             removed_node.pointer = None
#             self.length -= 1
#             return removed_node
#
#     """
#         1. Iterate through nodes from the beginning
#         2. Stop when pointer of the current iterating node points to tail (we now have the second to last node)
#         3. Set pointer of current iterating node to None
#         4. Set tail to that node
#         Time Complexity: O(n)
#     """
#
#     def pop_last(self):
#         pre = self.head
#         tmp = self.head
#
#         if self.head is None:
#             return None
#
#         if self.head == self.tail:
#             tmp = self.head
#             self.head = None
#             self.tail = None
#             self.length -= 1
#             return tmp
#
#         while tmp.pointer is not None:
#             pre = tmp
#             tmp = tmp.pointer
#             # print(f"pre: {pre.value} tmp: {tmp.value}")
#
#         pre.pointer = None
#         self.tail = pre
#         self.length -= 1
#         return tmp
#
#     def pop_last2(self):
#         tmp = self.head
#         result = None
#
#         if self.head is None:
#             return None
#
#         if self.head == self.tail:
#             tmp = self.head
#             self.head = None
#             self.tail = None
#             self.length -= 1
#             return tmp
#
#         while tmp.pointer.pointer is not None:
#             tmp = tmp.pointer
#
#         result = tmp.pointer
#         tmp.pointer = None
#         self.tail = tmp
#         self.length -= 1
#         return result
#
#
#     """
#     get_node(index): return node at index
#
#         lengtH: 3
#          5 -> 6 -> 9
#               ^
#         1. iterate through list using a counter
#         2. stop when counter is index, return node at that counter
#     """
#
#     def get_node(self, index) -> Union[Node, None]:
#         if index < 0 or index >= self.length:
#             return None
#         tmp = self.head
#         for _ in range(index):
#             tmp = tmp.pointer
#         return tmp
#
#
#     """
#         set_value (index, value)
#
#         5 -> 6 -> 9    =>    5 -> 18 -> 9
#              ^                    ^
#
#         1. Get node at index position using get(index)
#         2. Set value of that node to value
#     """
#
#     def set_value(self, value, index: int) -> bool:
#         if index < 0 or index >= self.length:
#             return False
#
#         target_node = self.get_node(index)
#         target_node.value = value
#         return True
#
#     """
#         index = 1
#         new node: 4->
#
#         5 -> 6 -> 9    =>    5 -> 4 -> 6 -> 9
#              ^
#             1. Create new node with value
#             2. get node before index position using get(index -1)
#                 3. Set new node's pointer to pointer of node before index
#                 4. Set pointer of node before index to new node.
#             5. Update length
#     """
#     def insert_value(self, value, index) -> bool:
#
#         if index < 0 or index > self.length:
#             return False
#         elif index == 0:
#             print("ok")
#             self.prepend(value)
#             return True
#         elif index == self.length:
#             self.append(value)
#             return True
#         else:
#             new_node = Node(value)
#             prev_node = self.get_node(index-1)
#             new_node.pointer = prev_node.pointer
#             prev_node.pointer = new_node
#             self.length += 1
#             return True
#
#     """
#         remove_node(index)
#
#         5 -> 6 -> 9    =>    5 -> 9
#              ^
#
#         1. Get previous node of index node (index -1), call it prev
#         2. get index node (index), call it tmp
#         3. Set pointer of prev node to pointer of tmp node
#
#     """
#     def remove_node(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         elif index == 0:
#             self.pop_first()
#             return True
#         elif index == self.length -1:
#             self.pop_last()
#             return True
#
#         prev = self.get_node(index -1)
#         tmp = self.get_node(index)
#         prev.pointer = tmp.pointer
#         self.length -= 1
#         return True
#
#     def reverse(self):
#
#         if self.head is None:
#             return False
#
#         curr = self.head
#         after = None
#         before = None
#
#         for _ in range(self.length):
#             after = curr.pointer  # Save the next node
#             curr.pointer = before  # Reverse the current node's pointer
#             before = curr  # Move 'before' to current node
#             curr = after  # Move 'curr' to the next node
#
#         self.head, self.tail = self.tail, self.head  # Swap head and tail after reversal
#         return True
#
#     def reverse2(self):
#
#         tmp = self.head
#         self.head, self.tail = self.tail, self.head
#         prev = None
#         aft = tmp.pointer
#
#         for _ in range(self.length):
#             print("*")
#             aft = tmp.pointer
#             tmp.pointer = prev
#             prev = tmp
#             tmp = aft
#
#     def pop_last_tmp(self):
#         if self.length == 0:
#             return None
#         returned_value = self.tail
#         if self.length == 1:
#             self.head, self.tail = None, None
#         else:
#             self.tail = self.tail.prev
#             self.tail.prev = None
#             returned_value.next = None
#         self.length -= 1
#         return returned_value
#
#     def pop_last_tmp2(self):
#         if self.length == 0:
#             return None
#         returned_value = self.tail
#         if self.length == 1:
#             self.head, self.tail = None, None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#         returned_value.prev = None
#         self.length -= 1
#         return returned_value
#
#
#
#
#
#
#
#     # def reverse(self):
#     #
#     #     if self.head is None:
#     #         return False
#     #
#     #     before = None
#     #     curr = self.head
#     #     after = curr.pointer
#     #     curr.pointer = before
#     #
#     #     while after is not None:
#     #         before = curr
#     #         curr = after
#     #         after = after.pointer
#     #         curr.pointer = before
#     #
#     #     tmp = self.head
#     #     self.head = self.tail
#     #     self.tail = tmp
#     #
#     #
#     #     # before = curr
#     #     # curr = after
#     #     # after = after.pointer
#     #     # print(f"before: {before.value} curr: {curr.value} after: {after.value}")
#     #     # curr.pointer = before
#     #     # print(f"curr -> {before.value}")
#     #     #
#     #     #
#     #     # before = curr
#     #     # curr = after
#     #     # after = after.pointer
#     #     # print(f"before: {before.value} curr: {curr.value} after: {after.value}")
#     #     # curr.pointer = before
#     #     # print(f"curr -> {before.value}")
#     #     #
#     #     # before = curr
#     #     # curr = after
#     #     # after = after.pointer
#     #     # print(f"before: {before.value} curr: {curr.value} after: {after}")
#     #     # curr.pointer = before
#     #     # print(f"curr -> {before.value}")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# linked_list = LinkedList(5)
# # print(f"head: {linked_list.head.value}  tail: {linked_list.tail.value}")
# linked_list.append(7)
# # print(f"head: {linked_list.head.value}  tail: {linked_list.tail.value}")
# linked_list.append(8)
# # print(f"head: {linked_list.head.value}  tail: {linked_list.tail.value}")
# linked_list.append(4)
# # print(f"head: {linked_list.head.value}  tail: {linked_list.tail.value}")
# linked_list.append(3)
# # print(f"head: {linked_list.head.value}  tail: {linked_list.tail.value}")
# linked_list.append(8)
# # print(f"head: {linked_list.head.value}  tail: {linked_list.tail.value}")
#
# linked_list.reverse2()
# linked_list.print()
#
#
#
#
#
#
#
#
