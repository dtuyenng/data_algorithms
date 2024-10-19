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
            self.head, self.tail = new_node

        new_node.next = self.head
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


dll = DoublyLinkedList(2)
dll.append(3)
dll.append(5)
dll.append(7)
dll.pop()
dll.pop()
dll.prepend(69)
dll.print()