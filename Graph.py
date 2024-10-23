class Graph():
    def __init__(self):
        self.adj_list = {}

    def print(self):
        for item, value in self.adj_list.items():
            print(item, ":",  value)

    def add_vertex(self, value):
        if value not in self.adj_list.keys():
            self.adj_list[value] = []
            return True
        print("Key already in list")
        return False

    def add_edge(self, vertex1: str, vertex2: str):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        print("One of the vertices not in list")
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            if vertex2 in self.adj_list[vertex1] and vertex1 in self.adj_listj_list[vertex2]:
                self.adj_list[vertex1].remove(vertex2)
                self.adj_list[vertex2].remove(vertex1)
                return True
        return False






graph = Graph()
graph.add_vertex("Montreal")
graph.add_vertex("Los Angeles")
graph.add_vertex("New York")

graph.add_edge("Montreal", "New York")
graph.print()
graph.remove_edge("Montreal", "Los Angeles")
graph.print()
