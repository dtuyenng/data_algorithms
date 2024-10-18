from typing import Union
"""
Linked List

Methods:
    print()
    append(value)
    prepend(value)
    pop_first(value)
    pop_last(value) 
    get(index)
    insert_value(value, index) *done*

"""
from operator import truediv


class Node:
    def __init__(self, value):
        self.value = value
        self.pointer = None


class LinkedList:
    def __init__(self, value):
        self.new_node = Node(value)
        self.head = self.new_node
        self.tail = self.new_node
        self.length = 1

    def print(self):
        temp_node = self.head
        print("Print")
        while temp_node is not None:
            print(f"{temp_node.value} -> ")
            temp_node = temp_node.pointer

    """ 
        1. Create a new node,
        2. Last node (currently tail) points to new node
        3. Tail points to it (new location of tail
        Time Complexity: O(1)
    """

    def append(self, value):
        node = Node(value)
        if self.head and self.tail is None:
            self.head =  node
            self.tail = node
        else:
            self.tail.pointer = node
            self.tail = node
            self.length += 1

    """
        1. Create new node
        2. Set new node point to head
        3. Set head to new node
        Time Complexity: O(1)
    
    """
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.pointer = self.head
            self.head = new_node
            self.length += 1


    """
        1. set node to be removed to head
        2. set head to removed node's pointer
        Time Complexity: 0(1)
    """

    def pop_first(self):

        if self.length == 1:
            removed_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_node
        elif self.length == 0:
            return None
        else:
            removed_node = self.head
            self.head = removed_node.pointer # or self.head = self.head.pointer
            removed_node.pointer = None
            self.length -= 1
            return removed_node

    """
        1. Iterate through nodes from the beginning
        2. Stop when pointer of the current iterating node points to tail (we now have the second to last node)
        3. Set pointer of current iterating node to None
        4. Set tail to that node
        Time Complexity: O(n)
    """

    def pop_last(self):
        pre = self.head
        tmp = self.head

        if self.head is None:
            return None

        if self.head == self.tail:
            tmp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return tmp

        while tmp.pointer is not None:
            pre = tmp
            tmp = tmp.pointer
            # print(f"pre: {pre.value} tmp: {tmp.value}")

        pre.pointer = None
        self.tail = pre
        print(f"tail set to {self.tail.value} with pointer {self.tail.pointer}")
        self.length -= 1
        return tmp

    def get(self, index: int) -> Union[Node, bool]:
        if index >= self.length or index < 0:
            return False
        counter = 0
        tmp_node = self.head
        while counter < index:
            tmp_node = tmp_node.pointer
            counter += 1
        return tmp_node

    """
    index = 1
    4-> 

    5 -> 6 -> 9    =>    5 -> 4 -> 6 -> 9
        1. Create new node with value
        2. Iterate through the list until node at index
        3. set new node's pointer to node at index
        4. set pre pointer  to new node
    """

    # def insert_value(self, index, value):
    #     new_node = Node(value)
    #
    #     if index < 0 or index > self.length:
    #         return None
    #     elif index == 0:
    #         self.prepend(value)
    #     elif index == self.length:
    #         self.append(value)
    #         print("yo")
    #     else:
    #         tmp = self.head
    #         pre = None
    #         for _ in range(index):
    #             pre = tmp
    #             tmp =tmp.pointer
    #
    #         new_node.pointer = tmp
    #         pre.pointer = new_node

    """
        index = 1
        4-> 

        5 -> 6 -> 9    =>    5 -> 4 -> 6 -> 9
            1. Create new node with value
            2. Iterate through the list until node before index (index -1)
            3. set that current node's pointer to new node
            4. set new node's pointer to current node.pointer
    """
    # def insert_value(self, index, value):
    #     new_node = Node(value)
    #
    #     if index < 0 or index > self.length:  # Invalid index
    #         return None
    #     elif index == 0:  # Insert at the start (equivalent to prepend)
    #         self.prepend(value)
    #         return
    #     elif index == self.length:  # Insert at the end (equivalent to append)
    #         self.append(value)
    #         return
    #     else:
    #         tmp = self.head
    #         for _ in range(index - 1):  # Stop at the node just before the target index
    #             tmp = tmp.pointer
    #
    #         new_node.pointer = tmp.pointer  # Point the new node to the next node
    #         tmp.pointer = new_node  # Insert new node after `tmp`
    #
    #     self.length += 1  # Increment length after successful insertion

    """
        index = 1
        new node: 4-> 
    
        5 -> 6 -> 9    =>    5 -> 4 -> 6 -> 9
        
            1. Create new node with value
            2. get node before index position using get(index -1)
                3. Set new node's pointer to pointer of node before index
                4. Set pointer of node before index to new node.
            5. Update length
    """
    def insert_value(self, value, index) -> bool:

        if index < 0 or index > self.length:
            return False
        elif index == 0:
            print("ok")
            self.prepend(value)
            return True
        elif index == self.length:
            self.append(value)
            return True
        else:
            new_node = Node(value)
            prev_node = self.get(index-1)
            new_node.pointer = prev_node.pointer
            prev_node.pointer = new_node
            self.length += 1



linked_list = LinkedList(5)
# print(f"head: {linked_list.head.value}  tail: {linked_list.tail.value}")
linked_list.append(7)
# print(f"head: {linked_list.head.value}  tail: {linked_list.tail.value}")
linked_list.append(8)
# print(f"head: {linked_list.head.value}  tail: {linked_list.tail.value}")
linked_list.append(4)
# print(f"head: {linked_list.head.value}  tail: {linked_list.tail.value}")
# linked_list.append(3)
# print(f"head: {linked_list.head.value}  tail: {linked_list.tail.value}")
# linked_list.append(8)
# print(f"head: {linked_list.head.value}  tail: {linked_list.tail.value}")

linked_list.print()
linked_list.insert_value(69, 3)
linked_list.print()






