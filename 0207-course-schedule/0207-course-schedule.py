class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        
        for course, preq in prerequisites:
            preMap[course].append(preq)
        
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            
            if preMap[course] == []:
                return True
            
            visited.add(course)
            for preq in preMap[course]:
                if not dfs(preq):
                    return False
            visited.remove(course)
            preMap[course] = []
            
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        
        return True
        