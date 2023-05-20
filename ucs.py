# from queue import PriorityQueue
#
# class Graph_ucs:
#     def __init__(self, directed=False):
#         self.graph = {}
#         self.directed = directed
#
#     def add_edge(self, start, end, cost):
#         if start in self.graph:
#             self.graph[start].append((end, cost))
#         else:
#             self.graph[start] = [(end, cost)]
#
#         if not self.directed:
#             if end in self.graph:
#                 self.graph[end].append((start, cost))
#             else:
#                 self.graph[end] = [(start, cost)]
#
#     def uniform_cost_search(self, start, goals):
#         visited = set()
#         frontier = PriorityQueue()
#         frontier.put((0, start, []))
#
#         while not frontier.empty():
#             cost, node, path = frontier.get()
#
#             if node in goals:
#                 return path + [node], node
#
#             if node not in visited:
#                 visited.add(node)
#                 neighbors = self.graph.get(node, [])
#                 for neighbor, neighbor_cost in neighbors:
#                     if neighbor not in visited:
#                         new_cost = cost + neighbor_cost
#                         frontier.put((new_cost, neighbor, path + [neighbor]))  # Fix here
#
#         return None, None
#
#     @staticmethod
#     def print_path(path, goal):
#         print(' -> '.join(path + [goal]))
#
#
#
from queue import PriorityQueue

class Graph_ucs:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_edge(self, start, end, cost):
        if start in self.graph:
            self.graph[start].append((end, cost))
        else:
            self.graph[start] = [(end, cost)]

        if not self.directed:
            if end in self.graph:
                self.graph[end].append((start, cost))
            else:
                self.graph[end] = [(start, cost)]

    def uniform_cost_search(self, start, goals):
        visited = set()
        frontier = PriorityQueue()
        frontier.put((0, start, []))

        while not frontier.empty():
            cost, node, path = frontier.get()

            if node in goals:
                return path + [node], node

            if node not in visited:
                visited.add(node)
                neighbors = self.graph.get(node, [])
                for neighbor, neighbor_cost in neighbors:
                    if neighbor not in visited:
                        new_cost = cost + neighbor_cost
                        frontier.put((new_cost, neighbor, path + [neighbor]))

        return None, None

    @staticmethod
    def print_path(path, goal):
        print(' -> '.join(path + [goal]))
