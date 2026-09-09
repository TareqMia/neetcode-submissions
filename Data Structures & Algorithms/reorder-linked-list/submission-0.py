# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        queue = collections.deque() 

        curr = head 

        while curr:
            queue.append(curr)
            curr = curr.next 

        dummy = ListNode(-1)
        curr = dummy

        turn = 0 
        while queue:
            node = queue.popleft() if turn % 2 == 0 else queue.pop()
            curr.next = node
            curr = curr.next 
            turn += 1  

        curr.next = None

        
        