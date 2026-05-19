class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        is_prereq = [[-1] * numCourses for _ in range(numCourses)]

        for prereq, course in prerequisites:
            adj[course].append(prereq)
            is_prereq[course][prereq] = True

        def dfs(course, prereq):
            if is_prereq[course][prereq] != -1:
                return is_prereq[course][prereq] == True
            
            for pre in adj[course]:
                if pre == prereq or dfs(pre, prereq):
                    is_prereq[course][prereq] = 1
                    return True
            is_prereq[course][prereq] = 0
            return False
        
        res = []
        for u, v in queries:
            res.append(dfs(v, u))
        
        return res