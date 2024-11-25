
import heapq

class Task:
    def __init__(self, task_id, task_name, priority):
        self.id = task_id
        self.name = task_name
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority


    def __gt__(self, other):
        return self.priority > other.priority

    def __eq__(self, other):
        return self.priority == other.priority


class TaskList:
    def __init__(self):
        self.id_counter = 1
        self.priority_list = []

    def add_task(self, task_name, priority):
        new_task = Task(self.id_counter, task_name, priority)
        # self.priority_list.insert(0, new_task)
        heapq.heappush(self.priority_list, new_task)
        self.id_counter += 1

    def print(self):
        for item in self.priority_list:
            print(item.id, item.name, item.priority)


todo = TaskList()
todo.add_task("Buy Milk", 61)
todo.add_task("Do Homework", 1)
todo.add_task("Wash Dishes", 2)

# print(todo.priority_list[1].priority)
# print(todo.priority_list[0].priority)
# print(todo.priority_list[1] < todo.priority_list[0])
todo.print()