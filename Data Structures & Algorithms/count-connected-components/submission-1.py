class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        components = 0 
        graph = collections.defaultdict(list)

        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        visited = set() 
        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited: 
                    dfs(neighbor)

        
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node) 

        return components



        


            