from collections import defaultdict 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.buildGraph(prerequisites)

        visited = set() 

        def dfs(course):

            if course in visited:
                return False 

            if len(graph[course]) == 0:
                return True 

            visited.add(course) 

            for preReq in graph[course]:
                if not dfs(preReq):
                    return False 

            visited.remove(course)
            graph[course] = [] 

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False 

        return True 


    def buildGraph(self, edges):
        graph = defaultdict(set)
        for course, preReq in edges:
            graph[preReq].add(course)
        return graph
        