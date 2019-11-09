import random


def partition(A: list, stt: int, end: int) -> int:
    x = A[stt]
    j = stt
    for i in range(stt + 1, end+1):
        if A[i] <= x:
            j += 1
            A[i], A[j] = A[j], A[i]
    A[stt], A[j] = A[j], A[stt]
    return j


def quick_select(A: list, stt: int, end: int, k: int):
    # Find the index of the k-th smallest number in A
    if k > 0 and end - stt + 1 >= k:
        p = random.randint(stt, end)
        A[stt], A[p] = A[p], A[stt]
        m = partition(A, stt, end)

        if m - stt + 1 == k:
            return A[m]
        if m - stt + 1 > k:
            return quick_select(A, stt, m-1, k)
        return quick_select(A, m+1, end, k - m + stt - 1)
    return -1

if __name__ == '__main__':
    A = [7, 10, 4, 3, 20, 15]
    k = 2
    stt = 0
    end = len(A)-1
    print("The k-th smallest element is:", quick_select(A, stt, end, k))
