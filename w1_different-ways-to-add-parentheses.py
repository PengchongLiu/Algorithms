# LeetCode 241
# https://leetcode.com/problems/different-ways-to-add-parentheses/


class Solution1:
    def __init__(self):
        import operator
        self.OPERATOR = {'+': operator.add, '-': operator.sub, '*': operator.mul}

    def diffWaysToCompute(self, input: str):
        if input.isdigit():
            return [int(input)]
        L = len(input)
        nums = []
        ops = []
        tmp = ""
        for i in range(L):
            c = input[i]
            if c not in "*-+":
                tmp += c
            else:
                ops.append(c)
                nums.append(int(tmp))
                tmp = ""
        nums.append(int(tmp))
        return self.DC(nums, ops)

    def DC(self, nums, ops):
        if len(nums) == 1:
            return nums
        res = []
        for i in range(len(nums)-1):
            left = self.DC(nums[:i+1], ops[:i])
            right = self.DC(nums[i+1:], ops[i+1:])

            for a in left:
                for b in right:
                    res.append(self.OPERATOR[ops[i]](a, b))

        return res


class Solution2:
    def diffWaysToCompute(self, input: str, memo={}):
        if input.isdigit():
            return [int(input)]
        if input in memo:
            return memo[input]
        res = []
        for i in range(len(input)):
            c = input[i]
            if c in "+-*":
                left = self.diffWaysToCompute(input[:i], memo)
                right = self.diffWaysToCompute(input[i+1:], memo)
                res += [eval(str(k)+input[i]+str(j)) for k in left for j in right]
        memo[input] = res
        return res


if __name__ == "__main__":
    # Solution1 seems faster than Solution2
    sol = Solution1()
    print(sol.diffWaysToCompute('2-1-1'))
    sol = Solution2()
    print(sol.diffWaysToCompute('2-1-1'))
