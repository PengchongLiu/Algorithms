# LeetCode 153
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


def findMin(nums) -> int:
    N = len(nums)
    stt = 0
    end = N-1
    if N == 1 or nums[end] > nums[0]:
        return nums[0]
    while stt <= end:
        mid = (stt+end)//2
        if nums[mid+1] < nums[mid]:
            return nums[mid+1]
        if nums[mid-1] > nums[mid]:
            return nums[mid]
        if nums[mid] < nums[stt]:
            end = mid - 1
        else:
            stt = mid

if __name__ == "__main__":
    print(findMin([4, 5, 6, 7, 0, 1, 2]))
