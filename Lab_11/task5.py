class Graph:
    def __init__(self):
        # Initialize an empty adjacency list
        self.adj_list = {}

    def add_edge(self, u, v):
        # Add an edge from u to v (undirected by default)
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):
        """
        Breadth-First Search (BFS) traversal from the start node.
        Returns a list of nodes in the order they are visited.
        """
        from collections import deque
        visited = set()           # Track visited nodes
        queue = deque([start])    # Queue for BFS
        order = []                # List to store traversal order

        while queue:
            node = queue.popleft()    # Dequeue the next node
            if node not in visited:
                visited.add(node)     # Mark node as visited
                order.append(node)    # Add to traversal order
                # Enqueue all unvisited neighbors
                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order

    def dfs_iterative(self, start):
        """
        Iterative Depth-First Search (DFS) traversal from the start node.
        Returns a list of nodes in the order they are visited.
        """
        visited = set()           # Track visited nodes
        stack = [start]           # Stack for DFS
        order = []                # List to store traversal order

        while stack:
            node = stack.pop()        # Pop the top node
            if node not in visited:
                visited.add(node)     # Mark node as visited
                order.append(node)    # Add to traversal order
                # Push all unvisited neighbors onto the stack
                # (reverse to maintain order similar to recursive DFS)
                for neighbor in reversed(self.adj_list.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

    def dfs_recursive(self, start):
        """
        Recursive Depth-First Search (DFS) traversal from the start node.
        Returns a list of nodes in the order they are visited.
        """
        order = []
        visited = set()

        def dfs(node):
            visited.add(node)         # Mark node as visited
            order.append(node)        # Add to traversal order
            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)     # Recurse on unvisited neighbors

        dfs(start)
        return order

# --- Example Usage and Comparison ---
if __name__ == "__main__":
    g = Graph()
    # Create a sample undirected graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(4, 5)

    print("Adjacency List:", g.adj_list)
    print("BFS from 0:", g.bfs(0))
    print("DFS Iterative from 0:", g.dfs_iterative(0))
    print("DFS Recursive from 0:", g.dfs_recursive(0))

    # Comparison Note:
    # - BFS explores neighbors level by level (uses a queue).
    # - Iterative DFS uses a stack to explore as deep as possible before backtracking.
    # - Recursive DFS uses the call stack for traversal, functionally similar to iterative DFS.
    # - For large/deep graphs, iterative DFS avoids Python's recursion limit.

