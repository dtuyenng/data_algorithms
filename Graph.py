from typing import Dict, List

class Graph:
    def __init__(self):
        self.adj_list: Dict[str, List] = {}

    def print_graph(self):
        print(" ")
        for vert in self.adj_list.items():
            print(vert)

    def add_vert(self, vert:str):
        if vert not in self.adj_list.keys():
            self.adj_list[vert] = []

    def add_edge(self, vert1: str, vert2: str):
        if vert1 in self.adj_list.keys() and vert2 in self.adj_list.keys():
            if vert1 not in self.adj_list[vert2] or vert2 not in self.adj_list[vert1]:
                self.adj_list[vert1].append(vert2)
                self.adj_list[vert2].append(vert1)
                return True
            else:
                print("Duplicate Edges")
                return False
        print("At least one of the vertices doesn't exist")
        return False

    def remove_edge(self, v1, v2):
        try:
            if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
                return True
        except ValueError:
            pass
        return False

    def remove_vert(self, vert):
        to_delete = self.adj_list[vert].copy()
        for item in to_delete:
            self.remove_edge(vert, item)
        self.adj_list.pop(vert)



graph = Graph()
graph.add_vert("A")
graph.add_vert("B")
graph.add_vert("C")
graph.add_vert("D")
graph.add_vert("E")

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("D", "A")
graph.add_edge("D", "B")
graph.add_edge("D", "C")
graph.remove_edge("E", "D")
graph.print_graph()






#
#
# class Graph:
#     def __init__(self):
#         self.adj_list = {}
#
#     def print(self):
#         for item, value in self.adj_list.items():
#             print(item, ":",  value)
#
#     def add_vertex(self, value):
#         if value not in self.adj_list.keys():
#             self.adj_list[value] = []
#             return True
#         print("Key already in list")
#         return False
#
#     def add_edge(self, vertex1: str, vertex2: str):
#         if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
#             self.adj_list[vertex1].append(vertex2)
#             self.adj_list[vertex2].append(vertex1)
#             return True
#         print("One of the vertices not in list")
#         return False
#
#     def remove_edge(self, vertex1, vertex2):
#         if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
#             if vertex2 in self.adj_list[vertex1] and vertex1 in self.adj_listj_list[vertex2]:
#                 self.adj_list[vertex1].remove(vertex2)
#                 self.adj_list[vertex2].remove(vertex1)
#                 return True
#         return False
#
#
#
#
#
#
# graph = Graph()
# graph.add_vertex("Montreal")
# graph.add_vertex("Los Angeles")
# graph.add_vertex("New York")
#
# graph.add_edge("Montreal", "New York")
# graph.print()
# graph.remove_edge("Montreal", "Los Angeles")
# graph.print()
