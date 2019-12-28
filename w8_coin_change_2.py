# LeetCode 518. https://leetcode.com/problems/coin-change-2/


class Solution:
    def change(self, amount: int, coins: list) -> int:
        if amount == 0:
            return 1
        N = len(coins)
        if N == 0:
            return 0

        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for coin in coins:
            for amt in range(coin, amount + 1):
                dp[amt] += dp[amt-coin]

        return dp[-1]

if __name__ == '__main__':
    amount = 10
    coins = [1, 2, 5]
    res = Solution().change(amount, coins)
    print(res)
