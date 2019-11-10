# LeetCode 53
# https://leetcode.com/problems/maximum-subarray/
from sys import maxsize


class Solution:
    def maxSubArray(self, nums) -> int:
        # O(N) solution
        N = len(nums)
        if N == 1:
            return nums[0]
        for i in range(1, N):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

    def DC(self, nums, stt, end):
        # Divide and Conquer
        N = len(nums)
        if N == 1:
            return nums[0]
        if stt > end:
            return -maxsize-1
        mid = (stt+end)//2
        maxL = 0
        s = 0
        for i in range(mid-1, stt-1, -1):
            s += nums[i]
            maxL = max(maxL, s)

        s = 0
        maxR = 0
        for i in range(mid+1, end+1):
            s += nums[i]
            maxR = max(maxR, s)

        return max(maxL+nums[mid]+maxR, self.DC(nums, stt, mid-1), self.DC(nums, mid+1, end))

if __name__ == "__main__":
    sol = Solution()
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(sol.maxSubArray(A))
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(sol.DC(A, 0, len(A)-1))
