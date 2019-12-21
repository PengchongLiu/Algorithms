# LeetCode 743: https://leetcode.com/problems/network-delay-time/
import heapq
from collections import defaultdict


class Solution:
    # 484 ms: using heapq for Q and defaultdict(dict) for S
    def networkDelayTime(self, times, N: int, K: int) -> int:
        # Dijkstra's algo to find longest time.
        graph = defaultdict(dict)
        for u, v, c in times:
            # graph[u].add((v, c))
            graph[u][v] = c

        Q = [(0, K)]
        S = {}
        while Q:
            du, u = heapq.heappop(Q)
            if u in S:
                continue
            S[u] = du
            for v in graph[u]:
                if v not in S:
                    heapq.heappush(Q, (du+graph[u][v], v))

        return max(S.values()) if len(S) == N else -1


class Solution2:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        d = defaultdict(dict)
        for i, j, k in times:
            d[i][j] = k
        pq = [(0, K)]
        visited = set()
        while pq:
            time, src = heapq.heappop(pq)
            visited.add(src)
            if len(visited) == N:
                return time
            for nxt in d[src]:
                if nxt not in visited:
                    heapq.heappush(pq, (time+d[src][nxt], nxt))
        return -1


if __name__ == '__main__':

    times = [[1, 2, 1], [2, 1, 3]]
    N = 2
    K = 2
    times = [[1, 2, 1], [2, 3, 2], [1, 3, 4]]
    N = 3
    K = 1

    sol = Solution()
    res = sol.networkDelayTime(times, N, K)
    print(res)
