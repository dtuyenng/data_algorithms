
class MaxHeap():
    def __init__(self):
        self.items = []
        self.size = 0

    def load_unsorted_array(self, array):
        self.items = array[:]
        self. size = len(self.items)

    def print(self):
        print(self.items)

    def left_child_index(self, index):
        return 2 * index + 1

    def right_child_index(self,index):
        return 2 * index + 2

    def load_unsorted_array(self, array):
        self.items = array[:]
        self.size = len(self.items)

    def print(self):
        output = self.items[0:self.size]
        print("Items", output)

    def left_child_index(self, index):
        return 2 * index + 1

    def right_child_index(self,index):
        return 2 * index + 2

    def parent_index(self, index):
        return (index - 1) // 2

    def swap(self, index1, index2):
        self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

    def extract_top(self):
        if self.size == 0:
            raise IndexError

        return_value = self.items[0]
        self.swap(0, self.size - 1)
        self.size -= 1
        self.max_heapify_down(0)
        return return_value

    def heap_sort(self):
        return_array = []
        for i in range(self.size):
            return_array.append(self.extract_top())
        return_array.reverse()

        print(return_array)




    def max_heapify_down(self, index):
        left = self.left_child_index(index)
        right = self.right_child_index(index)

        # Start by assuming the current index is the largest.
        largest_index = index

        # Check if the left child exists and is larger than the current node.
        if left < self.size and self.items[left] > self.items[largest_index]:
            largest_index = left

        # Check if the right child exists and is larger than the current largest.
        if right < self.size and self.items[right] > self.items[largest_index]:
            largest_index = right

        # Swap and recurse if the largest is not the current index.
        if largest_index != index:
            self.swap(largest_index, index)
            self.max_heapify_down(largest_index)

    def max_heapify_up(self, index):
        parent = self.parent_index(index)
        if parent >= 0:
            if self.items[parent] < self.items[index]:
                self.swap(index, parent)
                self.max_heapify_up(parent)


    def insert_node(self, value):
        #insert at the end of array
        self.items.append(value)
        self.size += 1
        self.max_heapify_up(self.size - 1)

    def build_max_heap(self):
        print("N: ", self.size)
        print("Internal: ", self.size // 2 - 1)
        for i in range(self.size // 2 - 1, -1, -1):
            self.max_heapify_down(i)



heap = MaxHeap()
# heap.load_unsorted_array([1, 14, 10, 8, 7, 9, 3, 2, 4, 6])
# heap.load_unsorted_array([10, 20, 15, 30 , 40])
# heap.load_unsorted_array([10, 20, 15, 30 , 40, 1, 17, 26, 99, 32])
heap.load_unsorted_array([10, 5, 9])
# print(heap.extract_top())
# print(heap.extract_top())
# print(heap.extract_top())
heap.heap_sort()




