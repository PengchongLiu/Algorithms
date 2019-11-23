# https://leetcode.com/problems/recover-binary-search-tree/
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # O(n) space
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # In an inorder traversal, nodes should go from smallest to largest.
        arr = []
        self.in_order(root, arr)
        to_switch = self.find_wrong_nodes(arr)
        to_switch[0].val, to_switch[1].val = to_switch[1].val, to_switch[0].val
        return root

    def in_order(self, root, arr):
        if not root:
            return []
        self.in_order(root.left, arr)
        arr += [root]
        self.in_order(root.right, arr)

    def find_wrong_nodes(self, arr):
        res = []
        for i in range(len(arr)):
            if not len(res):
                if arr[i].val > arr[i+1].val:
                    res.append(arr[i])
            else:
                if res[0].val < arr[i].val:
                    res.append(arr[i-1])
        if len(res) == 1:
            res.append(arr[-1])
        return res
