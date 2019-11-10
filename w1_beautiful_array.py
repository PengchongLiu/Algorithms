# LeetCode 932
# https://leetcode.com/problems/beautiful-array/
# https://leetcode.com/problems/beautiful-array/discuss/186679/C++JavaPython-Odd-+-Even-Pattern-O(N)


class Solution:
    def beautifulArray(self, N: int):
        res = [1]
        while len(res) < N:
            res = [i * 2 - 1 for i in res] + [i * 2 for i in res]
        return [i for i in res if i <= N]


if __name__ == "__main__":
    sol = Solution()
    N = 4
    print(sol.beautifulArray(N))
