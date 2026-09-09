"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        graph = collections.defaultdict() 

        def dfs(node):
            if not node:
                return None

            if node in graph:
                return graph[node] 

            copy = Node(node.val)
            graph[node] = copy

            for neighbor in node.neighbors:
                graph[node].neighbors.append(dfs(neighbor))

            # always return something in recursive dfs call
            return copy
        
        return dfs(node)

        


    
        