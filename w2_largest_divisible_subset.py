# LeetCode 368
# https://leetcode.com/problems/largest-divisible-subset/


from copy import copy


def largestDivisibleSubset(nums: list) -> list:
    nums.sort()
    N = len(nums)
    if N == 0:
        return []
    dp = [0 for i in range(N)]
    dp[0] = [nums[0]]
    for i in range(1, N):
        cur = nums[i]
        maxset = []
        for j in range(i):
            if cur % nums[j] == 0:
                subset = copy(dp[j])
                if len(subset) > len(maxset):
                    maxset = subset

        maxset.append(nums[i])
        dp[i] = maxset

    res = []
    for sub in dp:
        if len(sub) > len(res):
            res = sub
    return res
