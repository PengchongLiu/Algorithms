class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def __init__(self, method='bfs'):
        self.method = method.lower()
        super(Solution, self).__init__()

    def validTree(self, N, edges):
        # To be a valid tree, two conditions needs to be fulfilled:
        #   (1) no cyles; (2) no isolated node

        def bfs(adj: list, visited: list, parent: list) -> bool:
            # BFS method to check for cycles
            queue = [0]
            visited[0] = True
            while queue:
                node = queue.pop(0)
                for nb in adj[node]:
                    if not visited[nb]:
                        visited[nb] = True
                        queue.append(nb)
                        parent[nb] = node
                    elif parent[node] != nb:
                        return True
            return False

        def dfs(node: int, parent: int) -> bool:
            # DFS method to check for cycles
            # Returns True if has cycles else False
            if visited[node]:
                return True
            visited[node] = True
            for nb in adj[node]:
                if nb != parent and dfs(nb, node):
                    return True
            return False

        if len(edges) < N-1 or N == 0:
            return False

        # Construct adjacency list from undirected edges
        adj = [[] for _ in range(N)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # Search for cycles, return False if found any
        if self.method == 'dfs':
            visited = [False for _ in range(N)]
            if dfs(0, -1):
                return False
        else:
            visited = [False for _ in range(N)]
            parent = [-1 for _ in range(N)]
            if bfs(adj, visited, parent):
                return False

        # Return False if there's any isolated nodes
        if not all(visited):
            return False
        # Both conditions fulfilled, return True
        return True


if __name__ == "__main__":
    N = 5
    edges = [
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 4]
    ]

    sol = Solution(method='bfs')
    print(sol.validTree(N, edges))
