# LeetCode 210. https://leetcode.com/problems/course-schedule-ii/


class Solution():
    def findOrder(self, numCourses, prerequisites):
        # Kahn's TopoSort
        if numCourses <= 1:
            return True

        adj = [[] for _ in range(numCourses)]   # Adj list
        deg = [0 for _ in range(numCourses)]    # Deg count / num of prereq
        for e in prerequisites:
            adj[e[1]].append(e[0])
            deg[e[0]] += 1

        #DFS stack:
        # Start with courses that have no prereq
        order = []
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
                    order.append(nb)
        return order if (remaining == 0) else []


if __name__ == '__main__':
    sol = Solution()
    numCourses, prerequisites = 4, [[1, 0], [2, 0], [3, 1], [3, 2]]
    numCourses, prerequisites = 2, [[1, 0], [0, 1]]
    numCourses, prerequisites = 4, [[1, 0], [2, 0], [3, 1], [3, 2]]
    numCourses, prerequisites = 2, [[1, 0]]

    print(sol.findOrder(numCourses, prerequisites))
