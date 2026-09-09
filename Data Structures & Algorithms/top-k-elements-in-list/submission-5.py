class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums) 
        heap = [] 

        for f in freq:
            heapq.heappush(heap, (freq[f], f)) 

            if len(heap) > k:
                heapq.heappop(heap) 

        return [i[1] for i in heap]
        
        