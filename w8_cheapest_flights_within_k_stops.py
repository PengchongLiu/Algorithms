#LeetCode 787. https://leetcode.com/problems/cheapest-flights-within-k-stops/
from sys import maxsize
from collections import defaultdict


class Solution:
    def findCheapestPrice_DP(self, n: int, flights, src: int, dst: int, k: int) -> int:
        # Greedy DP --> slow, lots of duplicated visits
        # dp[v][j] -> minimum cost to node_u within j stops
        # dp[v][j] =  min(dp[u][j-1] + w_uv, du[u][j]), v is a neighbor of u
        if src == dst:
            return 0

        dp = [[maxsize for _ in range(k+2)] for _ in range(n)]
        for j in range(k + 2):
            dp[src][j] = 0
        for j in range(1, k+2):
            for u, v, w in flights:
                dp[v][j] = min(dp[u][j-1]+w, dp[v][j])
        return dp[dst][-1] if dp[dst][-1] < maxsize else -1

    def findCheapestPrice_BFS(self, n: int, flights, src: int, dst: int, k: int) -> int:
        # BFS --> fast
        if src == dst:
            return 0

        graph = defaultdict(dict)
        dp = [maxsize for _ in range(n)]
        for u, v, w in flights:
            graph[u][v] = w

        queue = [(src, -1, 0)]      # curNode, curStops, curCost

        while queue:
            u, s, c = queue.pop(0)  # curNode, curStops, curCost
            if u == dst or s == k:
                continue
            for v, w in graph[u].items():
                if c + w < dp[v]:
                    dp[v] = c+w
                    queue.append((v, s+1, dp[v]))
        return dp[dst] if dp[dst] < maxsize else -1


if __name__ == '__main__':
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    n = 11
    edges = [[5, 7, 4250], [8, 4, 8564], [7, 9, 5145], [5, 6, 974], [3, 10, 2626], [7, 0, 4533], [6, 9, 8181], [10, 4, 8331], [3, 2, 5223], [8, 10, 8342], [4, 0, 5683], [5, 10, 8848], [9, 10, 6415], [1, 4, 5031], [10, 0, 4782], [6, 5, 4003], [10, 3, 6335], [
        4, 9, 9133], [2, 5, 9870], [0, 10, 4406], [7, 3, 897], [9, 5, 8190], [7, 5, 9862], [2, 0, 2696], [7, 6, 9910], [0, 6, 3244], [0, 8, 3332], [1, 3, 4477], [8, 7, 9486], [6, 3, 246], [0, 3, 5373], [9, 6, 7210], [5, 1, 5804], [4, 1, 1434], [4, 8, 5625], [5, 0, 2894]]
    src = 4
    dst = 2
    k = 7
    res = Solution().findCheapestPrice_DP(n, edges, src, dst, k)
    print("DP:\n", res)
    res = Solution().findCheapestPrice_BFS(n, edges, src, dst, k)
    print("BFS:\n", res)
