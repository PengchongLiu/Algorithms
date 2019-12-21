# LeetCode 684. https://leetcode.com/problems/redundant-connection/


class DSU:
    def __init__(self, N):
        self.par = list(range(N+1))
        self.rnk = [0] * (N+1)

    def find(self, x):
        if self.par[x] != x:
            # Path compression
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        # Union by rank
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        # put the "shorter tree"(smaller rank) under ther higher tree
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges):
        dsu = DSU(len(edges))
        for edge in edges:
            if not dsu.union(*edge):
                return edge

if __name__ == '__main__':
    sol = Solution()
    edges = [[1, 2], [1, 3], [2, 3]]
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    res = sol.findRedundantConnection(edges)
    print(res)
