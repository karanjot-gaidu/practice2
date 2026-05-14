class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        cycle, visit = set(), set()
        output = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True


        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output