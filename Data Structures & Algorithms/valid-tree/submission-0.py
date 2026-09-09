class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False 

        graph = collections.defaultdict(list)

        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        visited = set() 

        def dfs(node):
            nonlocal visited

            if node in visited:
                return
            
            visited.add(node) 

            for otherNode in graph[node]:
                dfs(otherNode)

        dfs(0)

        return len(visited) == n

        