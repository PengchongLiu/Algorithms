import time


def partition(n: int) -> list:

    def search(n: int, k: int, cache: list) -> list:
        # search for partitions of n with largest element k
        if cache[n][k]:
            return cache[n][k]
        if n < k:
            return []
        if n == k:
            cache[n][k] = [[n]]
            return [[n]]
        if k == 1:
            cache[n][k] = [[1 for i in range(n)]]
            return [[1 for i in range(n)]]
        res = []
        for i in range(1, k+1):
            L = search(n-k, i, cache)
            L = map(lambda l: [k]+l, L)
            res.extend(L)
        cache[n][k] = res

        return res

    # Store the result of search(n,k) in cache[n][k]
    cache = [[[] for i in range(n+1)] for j in range(n+1)]

    res = []
    for i in range(1, n+1):
        A = search(n, i, cache)
        res.extend(A)

    return res


if __name__ == "__main__":

    num = int(input("Target = "))
    stt = time.time()
    res = partition(num)
    print("Time: %.2f ms" % ((time.time()-stt)*1000))
    print("Number of partitions:", len(res))
    print("All partitions:", sorted(res, reverse=True)[:20])
