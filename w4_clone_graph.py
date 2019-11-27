# https://leetcode.com/problems/clone-graph/
# This problem is weird


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        res = Node(node.val, [])
        to_visit = [node]
        visited = {node: res}
        while len(to_visit):
            n = to_visit.pop(0)
            curNode = visited[n]
            neighbors = []
            for nb in n.neighbors:
                if nb not in visited:
                    newNode = Node(nb.val, [])
                    visited[nb] = newNode
                    to_visit.append(nb)
                else:
                    newNode = visited[nb]
                neighbors.append(newNode)
            curNode.neighbors = neighbors
        return res
