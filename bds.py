class Graph_bds:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end):
        if start in self.graph:
            self.graph[start].append(end)
        else:
            self.graph[start] = [end]

    def bidirectional_search(self, start, goal):
        visited_forward = set()
        visited_backward = set()
        queue_forward = [start]
        queue_backward = [goal]

        while queue_forward and queue_backward:
            current_forward = queue_forward.pop(0)
            visited_forward.add(current_forward)

            if current_forward in visited_backward:
                return current_forward

            neighbors_forward = self.graph.get(current_forward, [])
            for neighbor in neighbors_forward:
                if neighbor not in visited_forward:
                    queue_forward.append(neighbor)

            current_backward = queue_backward.pop(0)
            visited_backward.add(current_backward)

            if current_backward in visited_forward:
                return current_backward

            neighbors_backward = self.graph.get(current_backward, [])
            for neighbor in neighbors_backward:
                if neighbor not in visited_backward:
                    queue_backward.append(neighbor)

        return None

    @staticmethod
    def print_path(path, goal):
        print(' -> '.join(path))