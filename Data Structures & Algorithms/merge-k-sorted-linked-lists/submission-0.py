# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        heap = []
        
        #insert nodes into heap
        for node in lists:
            if not node:
                continue
            
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
                
        dummy = ListNode(-1)
        curr = dummy
        
        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
            
        return dummy.next
        
        
        