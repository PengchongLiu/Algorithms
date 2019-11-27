# LeetCode 107
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/


class SolutionNaive:
    # BFS with recorded height
    def levelOrderBottom(self, root):
        if not root:
            return
        h = 1
        res = {}

        def traverse(root, h):
            if not root:
                return
            traverse(root.left, h+1)
            traverse(root.right, h+1)
            tmp = []
            if root.left:
                tmp.append(root.left.val)
            if root.right:
                tmp.append(root.right.val)
            if not tmp:
                return
            if h in res.keys():
                res[h] += tmp
            else:
                res[h] = tmp
            return

        traverse(root, h)
        res[0] = [root.val]
        key = sorted(res.keys(), reverse=True)
        res = [res[l] for l in key]
        return res


class Solution(object):
    # BFS with level matching
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        def traverse(root, level):
            if not root:
                return
            if len(res) == level:
                res.append([root.val])
            else:
                res[level].append(root.val)
            traverse(root.left, level+1)
            traverse(root.right, level+1)

        traverse(root, 0)
        res.reverse()
        return res
