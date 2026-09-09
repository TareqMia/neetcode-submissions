class Solution:

    """
    - use a minheap to store the elements of nums, based on the count 
    - pop from heap if length is over k
    
    """


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return [] 

        freq = collections.Counter(nums) 
        heap = [] 

        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))

            if len(heap) > k: 
                heapq.heappop(heap)

        return [i[1] for i in heap]
        