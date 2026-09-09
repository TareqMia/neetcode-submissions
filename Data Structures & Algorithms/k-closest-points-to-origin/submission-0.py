from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] 

        for x1,y1 in points:
            distance = sqrt((x1 - 0)**2 + (y1 - 0)**2)
            heapq.heappush(heap, (-distance, (x1, y1))) 

            if len(heap) > k:
                heapq.heappop(heap) 


        return [list(p[1]) for p in heap]