"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0 

        heap = [] 
        intervals.sort(key=lambda interval: interval.start)

        heap.append(intervals[0].end)

        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            if start >= heap[0]:
                heapq.heappop(heap)
                
                
            heapq.heappush(heap, end)

        return len(heap)
            


        