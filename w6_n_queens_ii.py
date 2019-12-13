# LeetCode 52: https://leetcode.com/problems/n-queens-ii/
class Solution:
    def __init__(self):
        super().__init__()
        self.res = 0

    def totalNQueens(self, n: int):
        if n <= 1:
            return n

        def getBoard(pos: list):
            board = []
            for p in pos:
                board.append('.'*(p)+'Q'+'.'*(n-p-1))
            return board

        def search(pos: list, t: int):
            if len(pos) == n:
                self.res += 1
                # res.append(pos)
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

    sol = Solution()
    n = 4
    res = sol.totalNQueens(4)
    print(res)
