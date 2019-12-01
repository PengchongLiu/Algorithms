# LeetCode 864 https://leetcode.com/problems/shortest-path-to-get-all-keys/


class Solution:
    def shortestPathAllKeys(self, grid) -> int:
        # Because grids can be visited more than once, we need some state-defining cache to store visited grids.
        # Here, we define the state by (coordinate i, coordinate j, collected keys, # of steps)
        # Then we use BFS with a Queue

        # Weird python tips:
        # It is much faster to use list/tuple than set/dict for key matching. Only tuple can be used in set (visited)
        # However, set is much faster for searching than list (visited = set())
        keys_all = [0 for _ in range(6)]
        for k in ''.join(grid):
            if k in "abcdef":
                keys_all[ord(k) - 97] = 1
        keys_all = tuple(keys_all)
        keys = tuple([0 for _ in range(6)])

        visited = set()
        Q = []
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == '@':
                    state = (i, j, keys, 0)
                    visited.add(state)
                    Q.append(state)
                    break
        nR = len(grid)
        nC = len(grid[0])
        while Q:
            i, j, keys, d = Q.pop(0)
            adj = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for i, j in adj:
                if 0 <= i < nR and 0 <= j < nC and grid[i][j] != '#':
                    g = grid[i][j]
                    if g in '.@':
                        state = (i, j, keys, d + 1)
                        if state not in visited:
                            visited.add(state)
                            Q.append(state)
                    elif g.isupper():
                        if keys[ord(g.lower()) - 97]:
                            state = (i, j, keys, d+1)
                            if state not in visited:
                                visited.add(state)
                                Q.append(state)
                    else: # g in 'abcdef':
                        keys_new = list(keys)
                        keys_new[ord(g)-97] = 1
                        keys_new = tuple(keys_new)
                        if keys_new == keys_all:
                            return d+1
                        state = (i, j, keys_new, d+1)
                        if state not in visited:
                            visited.add(state)
                            Q.append(state)
        return -1

if __name__ == "__main__":
    grid = ["@...a", ".###A", "b.BCc"]
    # grid = ["@abcdeABCDEFf"]
    grid = ["#..#.#.#..#.#.#.....#......#..", ".#.......#....#A.....#.#......", "#....#.....#.........#........", "...#.#.........#..@....#....#.", ".#.#.##...#.........##....#..#", "..........#..#..###....##..#.#", ".......#......#...#...#.....c#", ".#...#.##......#...#.###...#..", "..........##...#.......#......", "#...#.........a#....#.#.##....", "..#..#...#...#..#....#.....##.", "..........#...#.##............", "...#....#..#.........#..D.....", "....#E.#....##................", "...........##.#.......#.#....#",
            "...#..#...#.#............#e...", "..#####....#.#...........##..#", "##......##......#.#...#..#.#..", ".#F.......#..##.......#....#..", "............#....#..#..#...#..", ".............#...#f...#..##...", "....#..#...##.........#..#..#.", ".....#.....##.###..##.#......#", ".#..#.#...#.....#........###..", ".....#.#...#...#.....#.....#..", "##.....#....B.....#..#b.......", ".####....##..#.##..d.#......#.", "..#.....#....##........##...##", "...#...#...C..#..#....#.......", "#.....##.....#.#......#......."]
    print('-'*10)
    for i in grid:
        print(i)
    print('-'*10)
    sol = Solution()
    res = sol.shortestPathAllKeys(grid)
    print("Minimum number of steps:", res)
