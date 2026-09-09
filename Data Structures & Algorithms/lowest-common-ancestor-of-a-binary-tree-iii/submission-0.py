"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if not p or not q:
            return None
        s = set() 

        curr = p 

        while curr:
            s.add(curr)
            curr = curr.parent 

        curr = q 

        while curr:
            if curr in s:
                return curr

            curr = curr.parent

        return None

        