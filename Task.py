
import heapq

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __lt(self, other):
        if self.priority < other.priority:
            return True
    

