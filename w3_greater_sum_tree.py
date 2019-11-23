# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.res = 0
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.right)
        self.res += node.val
        node.val = self.res
        self.dfs(node.left)
        return node
