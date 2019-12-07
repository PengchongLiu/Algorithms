# LeetCode 37: https://leetcode.com/problems/sudoku-solver/
from collections import defaultdict


class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def search(i, j):
            # DFS with path restoration (backtracking)

            # Returns True when column is filled
            if i > 8:
                return True

            if j == 8:
                i_nxt = i + 1
                j_nxt = 0
            else:
                i_nxt = i
                j_nxt = j + 1

            if board[i][j] != '.':
                # DFS validity check
                return search(i_nxt, j_nxt)

            avails = digits - r[i] - c[j] - r[i//3, j//3]
            if not avails:
                return False

            for num in avails:
                board[i][j] = num
                r[i].add(num)
                c[j].add(num)
                r[i//3, j//3].add(num)

                if search(i_nxt, j_nxt):
                    return True
                else:   # Path Restoration
                    board[i][j] = '.'
                    r[i].remove(num)
                    c[j].remove(num)
                    r[i//3, j//3].remove(num)
            return False

        digits = set(map(str, range(1, 10)))

        # use r, c sets for rows and columns, and r also as the set for 3x3 box
        r, c = defaultdict(set), defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    r[i].add(board[i][j])
                    c[j].add(board[i][j])
                    r[i//3, j//3].add(board[i][j])

        search(0, 0)


if __name__ == "__main__":

    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    sol = Solution()
    res = sol.solveSudoku(board)
    for row in res:
        print(row)
