from max import largest


class MaxHeap:
    def __init__(self):
        # self.items = [0, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        # self.items = [0, 4, 10, 3, 5, 1]
        self.items = [0, 1, 5, 3, 10, 4]

        #############     1  2   3   4  5  6  7  8  9  10
        self.size = len(self.items) - 1

    def get_left_child_index(self, index) -> int:
        return 2 * index
    def get_right_child_index(self, index) -> int:
        return 2 * index + 1
    def get_parent_index(self, index):
        return int(index / 2)

    def has_left_child(self, index):
        return self.get_left_child_index(index) <= self.size
    def has_right_child(self, index):
        return self.get_right_child_index(index) <= self.size
    def has_parent(self, index) -> bool:
        return self.get_parent_index(index) > 1

    def left_child(self, index):
        return self.items[self.get_left_child_index(index)]
    def right_child(self, index):
        return self.items[self.get_right_child_index(index)]

    def insert(self, value):
        self.items.append(value)
        self.size += 1

    def swap(self, index1, index2):
        self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

    def print(self):
        print("Items:" , heap.items)

    def max_heapify(self, array, i):
        left = 2 * i
        right = 2 * i + 1

        # Find the largest between parent and left child
        if left <= self.size and array[left] > array[i]:
            biggest = left
        else:
            biggest = i

        # Compare the largest so far with the right child
        if right <= self.size and array[right] > array[biggest]:
            biggest = right

        # If the largest is not the parent, swap and recurse
        if biggest != i:
            print("bloop")
            array[i], array[biggest] = array[biggest], array[i]
            self.max_heapify(array, biggest)

    def build_max_heap(self):
        for i in range(self.size // 2, 0, -1):
            self.max_heapify(self.items, i)



heap = MaxHeap()
print("Heap Size(n) = ", heap.size)
heap.print()
heap.build_max_heap()
heap.print()


