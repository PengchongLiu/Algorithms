# Given N, k, s:
# Find find any k numbers in array [1,2,3,...,N] that Sum to s.


def kSum_naive(arr: list, k: int, s: int) -> list:
    from itertools import combinations
    # A naive solution to check the correctness of the DP solution
    res = []
    for nums in combinations(arr, k):
        if sum(nums) == s:
            res.append(list(nums))
    return res


def kSum_DP(arr: list, k: int, s: int, cur: list) -> list:
    '''
    Dynamic Programming solution: divide into subproblems until the summation of two.

    For k = 2:
        use the optimal solution of using two pointers.
    For k > 2:
        at each iteration, using the number arr[i],
        result[i, k, s] = result[i+1, k-1, s-arr[i]]

    Here we use a temporary list (cur: list) to store current combinations of numbers at current level of recursion.
    '''

    if k == 2:
        # An optimal solution using two pointers for the summation of two problem
        l, r = 0, len(arr)-1
        while l < r:
            su = arr[l]+arr[r]
            if su == s:
                res.append(cur + [arr[l], arr[r]])
                l += 1
                r -= 1
                while l < r and arr[l-1] == arr[l]:
                    l += 1
                while l < r and arr[r+1] == arr[r]:
                    r -= 1
            elif su < s:
                l += 1
            else:
                r -= 1
        return res

    # For k > 2 cases
    for i in range(len(arr) - k + 1):
        if arr[i - 1] != arr[i]:    # Skip duplicate items
            # pass the rest of the array into the next recursion
            kSum_DP(arr[i+1:], k-1, s-arr[i], cur+[arr[i]])
    return res


if __name__ == "__main__":
    '''
    Purpose: find all possible sets of k numbers in [1,2,...,N] that sum to s.
    '''

    N = 30
    s = 20
    k = 5
    arr = list(range(1, N + 1))

    assert k > 1, "Please make k>1"
    assert len(arr) >= k, "len(arr) < k"
    assert min(arr) <= s, "min(arr) > s"

    print(f"\n=======================================================================")
    print(f"Find all possible sets of {k} numbers in [1, 2, ... ,{N}] that sum to {s}:")
    print(f"=======================================================================\n")

    res = []
    res = kSum_naive(arr, k, s)
    print("Naive Solution:\n")
    print(res)
    print(f"\n-----------------------------------------------------------------------\n")
    res = []
    print("DP Solution:\n")
    res = kSum_DP(arr, k, s, [])
    print(res)
    print(f"\n=======================================================================")
