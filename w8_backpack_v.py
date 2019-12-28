# LintCode 563. https://www.lintcode.com/problem/backpack-v/description


class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """

    def backPackV_naive(self, nums, target):
        # Naive DP using 2D list --> memory limit exceeded
        N = len(nums)
        if N == 0:
            return 0

        # dp[i][j] --> ways of summing up to j using first i items
        # dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j]
        # dp[i][0] = 1
        # dp[0][j] = 1
        dp = [[0 for _ in range(target+1)] for _ in range(N)]
        for i in range(N):
            dp[i][0] = 1
        for i in range(N):
            for j in range(1, target + 1):
                dp[i][j] = dp[i-1][j]
                if j - nums[i] >= 0:
                    dp[i][j] += dp[i-1][j-nums[i]]
        return dp[-1][-1]

    def backPackV(self, nums, target):
        # DP using 1D list --> memory optimized
        N = len(nums)
        if N == 0:
            return 0
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(N):
            for j in range(target, nums[i] - 1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[-1]

if __name__ == '__main__':
    nums = [1, 2, 3, 3, 7]
    target = 7
    nums = [1, 2, 3]
    target = 3
    nums = [81, 112, 609, 341, 164, 601, 97, 709, 944, 828, 627, 730, 460, 523, 643, 901, 602, 508, 401, 442, 738, 443, 555, 471, 97, 644, 184, 964, 418, 492, 920, 897, 99, 711, 916, 178, 189, 202, 72, 692, 86, 716, 588, 297, 512, 605, 209, 100, 107, 938, 246, 251, 921, 767, 825,
            133, 465, 224, 807, 455, 179, 436, 201, 842, 325, 694, 132, 891, 973, 107, 284, 203, 272, 538, 137, 248, 329, 234, 175, 108, 745, 708, 453, 101, 823, 937, 639, 485, 524, 660, 873, 367, 153, 191, 756, 162, 50, 267, 166, 996, 552, 675, 383, 615, 985, 339, 868, 393, 178, 932]
    target = 80000
    res = Solution().backPackV(nums, target)
    print(res)
