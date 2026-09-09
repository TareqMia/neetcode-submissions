class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        d = {} 

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                return sorted([i, d[complement]])

            else:
                d[nums[i]] = i

        return []

        