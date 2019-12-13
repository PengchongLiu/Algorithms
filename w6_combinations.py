# LeetCode 77. https://leetcode.com/problems/combinations/


class Solution:
    def combine(self, n: int, k: int):
        if n == 0 or n < k:
            return []

        res = []

        #def search(cur: list, nxt: list):
        #    # Naive backtracking
        #    if len(cur) == k:
        #        res.append(cur)
        #    elif nxt:
        #        search(cur+[nxt[0]], nxt[1:])
        #        search(cur, nxt[1:])
        #    return
        #search([], list(range(1, n+1)))

        def search(comb: list, n: int, k: int):
            # Fast solution
            if k == 0:
                res.append(comb)
            else:
                for i in range(1, n+1):
                    search(comb+[i], i-1, k-1)
        search([], n, k)
        return res


if __name__ == "__main__":
    sol = Solution()
    res = sol.combine(5, 3)
    print(res)
