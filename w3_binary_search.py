def search(arr: list, target: int):
    N = len(arr)
    if N == 0:
        return -1
    if N == 1 and arr[0] != target:
        return -1

    l, r = 0, N-1

    while l < r:
        mid = l + (r-l)//2
        if arr[mid] == target:
            while arr[mid] == target:
                # Leftmost
                mid -= 1
                # Rightmost
                # mid += 1
            return mid+1
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6]
    target = 5
    res = search(arr, target)
    if res >= 0:
        print(res, arr[res])
    else:
        print('Not found')
