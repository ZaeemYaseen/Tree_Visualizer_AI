class Graph_dfs:
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

    def depth_first_search(self, start, goals):
        visited = set()
        stack = [(start, [])]

        while stack:
            node, path = stack.pop()

            if node in goals:
                return path, node

            if node not in visited:
                visited.add(node)
                neighbors = self.graph.get(node, [])
                for neighbor in neighbors:
                    stack.append((neighbor, path + [neighbor]))

        return None, None

    @staticmethod
    def print_path(path, goal):
        print(' -> '.join(path + [goal]))
