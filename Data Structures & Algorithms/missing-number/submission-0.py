class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        return abs(sum(nums) - sum([i for i in range(len(nums) + 1)]))
        