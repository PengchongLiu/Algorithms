# LeetCode 200: https://leetcode.com/problems/number-of-islands/
# The number of island is essentially the number of connected subgraphs


class Solution:
    def numIslands(self, grid):
        nR = len(grid)
        if nR == 0:
            return 0
        nC = len(grid[0])

        res = 0

        for r in range(nR):
            for c in range(nC):

                if grid[r][c] != '1':
                    continue

                # DFS traversal of all connected grids.
                # Whenever a connected node is visited, mark it with '-' to avoid duplicated visits
                res += 1
                grid[r][c] = '-'
                stack = [(r, c)]
                while stack:
                    i, j = stack.pop()
                    adj = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                    for i, j in adj:
                        if 0 <= i < nR and 0 <= j < nC and grid[i][j] == '1':
                            grid[i][j] = '-'
                            stack.append((i, j))

        return res


if __name__ == "__main__":

    inp = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]

    print("==== Input Grid ====")
    for i in inp:
        print("".join(i))

    sol = Solution()
    res = sol.numIslands(inp)

    print("==== Final Grid ====")
    for i in inp:
        print("".join(i))
    print("==== Island Count ====")
    print(res)
