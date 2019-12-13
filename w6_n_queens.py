# LeetCode 51: https://leetcode.com/problems/n-queens/
class Solution:
    def __init__(self):
        super().__init__()
        self.res = []

    def solveNQueens(self, n: int):
        if n <= 0:
            return []
        if n == 1:
            return ['Q']

        def getBoard(pos: list):
            board = []
            for p in pos:
                board.append('.'*(p)+'Q'+'.'*(n-p-1))
            return board

        def search(pos: list, t: int):
            if len(pos) == n:
                self.res.append(getBoard(pos))
            else:
                for i in range(n):
                    # Check column
                    if i in pos:
                        continue
                    # Check diagonal and anti-diagonal:
                    flag = False
                    for r, c in enumerate(pos):
                        if (r - c == len(pos) - i) or (r + c == len(pos) + i):
                            flag = True
                            break
                    if flag:
                        continue

                    # Iterate each column at current row = len(pos) - 1
                    search(pos+[i], i)
            return

        search([], -1)
        return self.res

if __name__ == "__main__":

    def printBoard(board: list):
        print('='*(n+4))
        for row in board:
            print(' ', row)
        print('='*(n+4))

    sol = Solution()
    n = 4
    res = sol.solveNQueens(4)
    for r in res:
        printBoard(r)
