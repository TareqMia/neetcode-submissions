class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return [] 

        freq = collections.Counter(nums)
        buckets = [set() for _ in range(len(nums) + 1)]

        for num in nums:
            f = freq[num] 
            buckets[f].add(num)

        result = [] 
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result


        