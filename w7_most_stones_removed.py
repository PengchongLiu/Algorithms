# LeetCdoe 947: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/


class Solution:
    def removeStones(self, stones):

        N = len(stones)
        if N <= 1:
            return 0

        self.par = list(range(N))   # parents of stone idx
        self.rnk = [0] * (N)
        self.cnt = 0
        rows = {}   # find parent in row
        cols = {}   # find parent in column
        for i, (r, c) in enumerate(stones):
            if r not in rows:
                rows[r] = i
            if c not in cols:
                cols[c] = i
            self.union(rows[r], i)
            self.union(cols[c], i)
        return self.cnt

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
        if self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        self.cnt += 1
        return True


def drawGrid(stones):
    print("Grid:")
    row = [x[0] for x in stones]
    col = [x[1] for x in stones]
    dim = max(max(row), max(col))+1
    grid = [['*' for _ in range(dim)] for _ in range(dim)]
    for i, (r, c) in enumerate(stones):
        grid[r][c] = str(i)

    for g in grid:
        print(g)
    print()

if __name__ == '__main__':
    sol = Solution()
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
    stones = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 1], [2, 2], [3, 2], [3, 3], [3, 4], [4, 3], [4, 4]]
    stones = [[0, 1], [1, 2], [1, 3], [3, 3], [2, 3], [0, 2]]
    drawGrid(stones)

    res = sol.removeStones(stones)
    print(res)
    print(sol.par)
    print(sol.rnk)
