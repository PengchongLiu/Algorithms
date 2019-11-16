def palindrome(s: str, l: int, r: int, cache: list) -> int:
    # Dynamic programming with memoization
    # cache[l][r] is the solution for string[l:r+1]
    if cache[l][r] is not None:
        return cache[l][r]
    if l == r:
        cache[l][r] = 0
    elif l == r - 1:
        cache[l][r] = 0 if s[l] == s[r] else 1
    elif s[l] == s[r]:
        cache[l][r] = palindrome(s, l+1, r-1, cache)
    else:
        cache[l][r] = min(palindrome(s, l+1, r, cache), palindrome(s, l, r-1, cache)) + 1
    return cache[l][r]

if __name__ == "__main__":
    s = 'Qishi'
    N = len(s)
    cache = [[None for _ in range(N)] for _ in range(N)]
    print(palindrome(s, 0, N-1, cache))
    # print(cache)
