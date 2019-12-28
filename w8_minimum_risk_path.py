# LintCode 783: https://www.lintcode.com/problem/minimum-risk-path/description
# Kuskal's MST


class Solution:
    """
    @param n: maximum index of position.
    @param m: the number of undirected edges.
    @param x:
    @param y:
    @param w:
    @return: return the minimum risk value.
    """

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.par[xr] = yr
        return True

    def getMinRiskValue(self, n, m, x, y, w):
        # Kuskal's MST between 0 and n
        self.par = list(range(n+1))
        edges = []

        for i in range(m):
            edges.append((w[i], x[i], y[i]))
        edges = sorted(edges)

        res = 0
        while self.find(0) != self.find(n):
            c, u, v = edges.pop(0)
            if self.union(u, v):
                res = max(res, c)
            if not edges:
                break

        return res


if __name__ == '__main__':
    n = 2
    m = 2
    x = [0, 1]
    y = [1, 2]
    w = [1, 2]
    n = 3
    m = 4
    x = [0, 0, 1, 2]
    y = [1, 2, 3, 3]
    w = [1, 2, 3, 4]
    res = Solution().getMinRiskValue(n, m, x, y, w)
    print(res)
