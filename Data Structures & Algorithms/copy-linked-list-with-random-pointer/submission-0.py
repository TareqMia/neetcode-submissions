"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None 

        mapping = { None: None } 

        curr = head 

        while curr:
            copy = Node(curr.val)
            mapping[curr] = copy 
            curr = curr.next 

        curr = head 

        while curr:
            node = mapping[curr] 
            node.next = mapping[curr.next]
            node.random = mapping[curr.random]

            curr = curr.next 

        return mapping[head]

        