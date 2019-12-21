# LeetCode 207. https://leetcode.com/problems/course-schedule/
# A good reference: https://leetcode.com/problems/course-schedule/discuss/441722/Python-99-time-and-100-space.-Collection-of-solutions-with-explanation


class Solution():
    def canFinish(self, numCourses, prerequisites):
        # DFS to detect cycles
        if numCourses <= 1:
            return True

        adj = [[] for _ in range(numCourses)]   # Adj list
        for e in prerequisites:
            adj[e[1]].append(e[0])

        def isCyclic(adj, node):
            if not visited[node]:
                visited[node] = True
                recStack[node] = True
                for nb in adj[node]:
                    if (not visited[nb]) and isCyclic(adj, nb):
                        return True
                    elif recStack[nb]:
                        return True
            recStack[node] = False
            return False

        visited = [False] * len(adj)
        recStack = [False] * len(adj)
        for node in range(len(adj)):
            if isCyclic(adj, node):
                return False
        return True

    def canFinish2(self, numCourses, prerequisites):
        # https://leetcode.com/problems/course-schedule/discuss/441722/Python-99-time-and-100-space.-Collection-of-solutions-with-explanation
        # Kahn's TopoSort --> fast
        if numCourses <= 1:
            return True

        adj = [[] for _ in range(numCourses)]   # Adj list
        deg = [0 for _ in range(numCourses)]    # Deg count / num of prereq
        for e in prerequisites:
            adj[e[1]].append(e[0])
            deg[e[0]] += 1

        #DFS stack:
        # Start with courses that have no prereq
        stack = [n for n in range(numCourses) if deg[n] == 0]
        # Keep count of the remaining prereq pair
        remaining = len(prerequisites)
        while stack:
            node = stack.pop()
            for nb in adj[node]:
                remaining -= 1
                deg[nb] -= 1        # One prereq is fulfilled
                if deg[nb] == 0:    # If all prereq fullfiled, explore its nb
                    stack.append(nb)
        return remaining == 0


if __name__ == '__main__':
    sol = Solution()
    numCourses, prerequisites = 4, [[1, 0], [2, 0], [3, 2], [2, 1]]
    numCourses, prerequisites = 4, [[1, 0], [2, 0], [3, 1], [3, 2]]
    numCourses, prerequisites = 2, [[1, 0], [0, 1]]

    print(sol.canFinish(numCourses, prerequisites))
