import math
from collections import deque

class Graph_best_first:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_edge(self, start, end, weight):
        if start in self.graph:
            self.graph[start].append((end, weight))
        else:
            self.graph[start] = [(end, weight)]

        if not self.directed:
            if end in self.graph:
                self.graph[end].append((start, weight))
            else:
                self.graph[end] = [(start, weight)]

    def heuristic(self, node, goal):
        # Calculate the Euclidean distance between the current node and the goal node
        x1, y1 = node
        x2, y2 = goal
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def best_first_search(self, start, goal):
        visited = set()
        queue = deque()
        queue.append((start, [], 0))  # (node, path, cost)

        while queue:
            node, path, cost = queue.popleft()

            if node == goal:
                return path, node

            if node not in visited:
                visited.add(node)
                neighbors = self.graph.get(node, [])
                for neighbor, weight in neighbors:
                    new_cost = cost + weight
                    # Calculate the heuristic value for the neighbor
                    h = self.heuristic(neighbor, goal)
                    queue.append((neighbor, path + [neighbor], new_cost))

                # Sort the queue based on the heuristic value
                queue = deque(sorted(queue, key=lambda x: self.heuristic(x[0], goal)))

        return None, None

    @staticmethod
    def print_path(path, goal):
        print(' -> '.join(path))
