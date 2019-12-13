# LeetCode 784: https://leetcode.com/problems/letter-case-permutation/
# BackTracking + binary tree


class Solution:
    def letterCasePermutation(self, S: str):

        L = len(S)
        if not L:
            return []

        res = []

        def search(cur: str, nxt: str):

            if not nxt:
                res.append(cur)
            else:
                search(cur+nxt[0], nxt[1:])
                if nxt[0].islower():
                    search(cur+nxt[0].upper(), nxt[1:])
                elif nxt[0].isupper():
                    search(cur+nxt[0].lower(), nxt[1:])

            return

        search("", S)
        return res

if __name__ == "__main__":
    sol = Solution()
    S = "12345"
    S = "a1b2"
    res = sol.letterCasePermutation(S)
    print(res)
