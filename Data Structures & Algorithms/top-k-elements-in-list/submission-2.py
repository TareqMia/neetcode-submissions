class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return [] 

        freq = collections.Counter(nums) 
        heap = [] 

        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))

            if len(heap) > k: 
                heapq.heappop(heap)

        
        result = [] 

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
        