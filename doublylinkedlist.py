from select import select
from types import new_class


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        self.new_node = Node(value)
        self.head = self.new_node
        self.tail = self.new_node
        self.length = 1


    def print(self):
        tmp_node = self.head
        while tmp_node is not None:
            print(f"{tmp_node.value} -> ")
            tmp_node = tmp_node.next
        print(f"Length: {self.length}")

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head, self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return False
        tmp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        tmp.prev = None
        self.length -= 1
        return True

    def pop_first(self):
        if self.head is None:
            return False
        elif self.head == self.tail:
            self.head, self.tail = None, None
            self.length -= 1
            return True
        else:
            tmp = self.head
            self.head = self.head.next
            self.head.prev = None
            tmp.next = None
            self.length -= 1
            return tmp

    def get(self, index):
        if index < 0 or index >= self.length:
            print("Index out of range")
            return None
        tmp = self.tail
        if index < self.length / 2:
            tmp = self.head
            # print("lower")
            for _ in range(index):
                tmp = tmp.next
        else:
            tmp = self.tail
            # print("higher")
            for _ in range(self.length-1, index, -1):
                tmp = tmp.prev
        print(f"get: {tmp.value}")
        return tmp

    def insert_withoutget(self, value, index):
        new_node = Node(value)
        tmp = self.head
        for _ in range(index):
            tmp = tmp.next

        new_node.next = tmp
        new_node.prev = tmp.prev
        tmp2 = tmp.prev
        tmp.prev = new_node
        tmp2.next = new_node
        self.length += 1

    def insert(self, value, index):
        new_node = Node(value)
        if self.head is None:
            return False
        elif self.head == self.tail:
            self.head, self.tail = None, None
            self.length += 1
            return True
        elif index == 0:
            self.prepend(value)
            return True
        elif index == self.length - 1:
            self.pop()
            return True
        else:
            tmp = self.get(index)
            tmp2 = tmp.prev
            new_node.prev = tmp.prev
            tmp2.next = new_node
            new_node.next = tmp
            tmp.prev = new_node
            self.length += 1




    def set_value(self, value, index):
        selected_node = self.get(index)
        selected_node.value = value
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            self.pop_first()
            self.length -= 1
            return True
        elif index == self.length -1:
            self.pop()
            self.length -= 1
            return True
        else:
            selected_node = self.get(index)
            previous_node = selected_node.prev
            next_node = selected_node.next
            previous_node.next = selected_node.next
            next_node.prev = previous_node
            selected_node.next = None
            selected_node.prev = None
            self.length -= 1




dll = DoublyLinkedList(2)
dll.append(3)
dll.append(5)
dll.append(7)
dll.prepend(69)
dll.insert(96, 0)
dll.print()


