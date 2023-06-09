class Graph_dls:
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

    def depth_limited_search(self, start, goals, depth_limit):
        visited = set()
        stack = [(start, [], 0)]

        while stack:
            node, path, depth = stack.pop()

            if node in goals or depth ==depth_limit:
                return path, node

            if depth < depth_limit and node not in visited:
                visited.add(node)
                neighbors = self.graph.get(node, [])
                for neighbor in neighbors:
                    stack.append((neighbor, path + [neighbor], depth + 1))

        return None, None

    @staticmethod
    def print_path(path, goal):
        print(' -> '.join(path + [goal]))
