# class Graph_bfs:
#     def __init__(self, graph):
#         """
#         Initializes the Graph_bfs class with the input graph.
#
#         Args:
#             graph (dict): A dictionary representing the graph as an adjacency list.
#         """
#         self.graph = graph
#
#     def bfs(self, start):
#         """
#         Performs breadth-first search on the graph starting from the specified vertex.
#
#         Args:
#             start (str): The starting vertex for the search.
#
#         Returns:
#             list: A list of vertices in the order they were visited during the search.
#         """
#         visited = []  # To keep track of visited vertices
#         queue = [start]  # Initialize a queue with the starting vertex
#
#         while queue:
#             vertex = queue.pop(0)  # Dequeue a vertex from the front of the queue
#             if vertex not in visited:
#                 visited.append(vertex)  # Mark the vertex as visited
#                 neighbors = self.graph[vertex]  # Get the neighbors of the vertex
#                 for neighbor in neighbors:
#                     queue.append(neighbor)  # Enqueue each unvisited neighbor
#
#         return visited
#
# from collections import defaultdict
#
#
# class Graph_bfs:
#     def __init__(self, directed=False):
#         self.graph = defaultdict(list)
#         self.directed = directed
#
#     def add_edge(self, node1, node2):
#         self.graph[node1].append(node2)
#         if not self.directed:
#             self.graph[node2].append(node1)
#
#     def breadth_first_search(self, start, goals):
#         visited = set()
#         queue = [[start]]
#
#         while queue:
#             path = queue.pop(0)
#             node = path[-1]
#
#             if node in goals:
#                 return path, node
#
#             if node not in visited:
#                 neighbors = self.graph[node]
#                 for neighbor in neighbors:
#                     new_path = list(path)
#                     new_path.append(neighbor)
#                     queue.append(new_path)
#
#                 visited.add(node)
#
#         return None, None


from collections import deque

class Graph_bfs:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_edge(self, start, end):
        if start in self.graph:
            self.graph[start].append(end)
        else:
            self.graph[start] = [end]

        if not self.directed:
            if end in self.graph:
                self.graph[end].append(start)
            else:
                self.graph[end] = [start]

    def breadth_first_search(self, start, goals):
        visited = set()
        queue = deque()
        queue.append((start, []))

        while queue:
            node, path = queue.popleft()

            if node in goals:
                return path, node

            if node not in visited:
                visited.add(node)
                neighbors = self.graph.get(node, [])
                for neighbor in neighbors:
                    queue.append((neighbor, path + [neighbor]))

        return None, None

    @staticmethod
    def print_path(path, goal):
        print(' -> '.join(path + [goal]))
