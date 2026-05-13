class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        visiting = set()
        
        def dfs(course):
            if course in visiting:
                return False
            
            if graph[course] == []:
                return True
            
            visiting.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
                
            visiting.remove(course)
            graph[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True