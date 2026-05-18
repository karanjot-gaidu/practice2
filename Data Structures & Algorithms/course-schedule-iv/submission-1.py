class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        for prereq, course in prerequisites:
            adj[course].append(prereq)

        def dfs(course):
            if course not in prereq_map:
                prereq_map[course] = set()
                for prereq in adj[course]:
                    prereq_map[course] |= dfs(prereq)
                prereq_map[course].add(course)
            return prereq_map[course]
        
        prereq_map = {}
        for course in range(numCourses):
            dfs(course)
        res = []
        for u, v in queries:
            res.append(u in prereq_map[v])
        return res