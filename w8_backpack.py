# Lintcode 92. https://www.lintcode.com/problem/backpack/description


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):

        n = len(A)
        if n == 0:
            return 0

        # dp[j] --> the max size up to size-j
        dp = [0 for _ in range(m+1)]

        for i in range(n):
            for j in range(m, A[i]-1, -1):
                dp[j] = max(dp[j], dp[j-A[i]]+A[i])
        return dp[-1]


if __name__ == '__main__':
    m = 10
    A = [3, 4, 8, 5]
    res = Solution().backPack(m, A)
    print('DP:\n', res)
