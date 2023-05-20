class Graph_ids:
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

    def iterative_deepening_search(self, start, goals):
        depth_limit = 0
        while True:
            visited = set()
            stack = [(start, [])]

            while stack:
                node, path = stack.pop()

                if node in goals:
                    return path + [node], node

                if len(path) <= depth_limit:
                    visited.add(node)
                    neighbors = self.graph.get(node, [])
                    for neighbor in neighbors:
                        if neighbor not in visited and neighbor not in [item[0] for item in stack]:
                            stack.append((neighbor, path + [node]))

            depth_limit += 1

            if depth_limit > len(self.graph):
                # If depth_limit exceeds the number of nodes in the graph, terminate the search
                break

        return None, None

    @staticmethod
    def print_path(path, goal):
        print(' -> '.join(path))
