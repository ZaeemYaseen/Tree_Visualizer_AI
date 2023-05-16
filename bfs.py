class Graph_bfs:
    def __init__(self, graph):
        pass
    #     """
    #     Initializes the Graph_bfs class with the input graph.
    #
    #     Args:
    #         graph (dict): A dictionary representing the graph as an adjacency list.
    #     """
    #     self.graph = graph
    #
    # def bfs(self, start):
    #     """
    #     Performs breadth-first search on the graph starting from the specified vertex.
    #
    #     Args:
    #         start (str): The starting vertex for the search.
    #
    #     Returns:
    #         list: A list of vertices in the order they were visited during the search.
    #     """
    #     visited = []  # To keep track of visited vertices
    #     queue = [start]  # Initialize a queue with the starting vertex
    #
    #     while queue:
    #         vertex = queue.pop(0)  # Dequeue a vertex from the front of the queue
    #         if vertex not in visited:
    #             visited.append(vertex)  # Mark the vertex as visited
    #             neighbors = self.graph[vertex]  # Get the neighbors of the vertex
    #             for neighbor in neighbors:
    #                 queue.append(neighbor)  # Enqueue each unvisited neighbor
    #
    #     return visited
