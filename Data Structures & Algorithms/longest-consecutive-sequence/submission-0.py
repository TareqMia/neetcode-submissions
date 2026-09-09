class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums: 
            return 0

        s = set(nums) 
        maxx = float("-inf")


        for num in nums:
            if num - 1 not in s:
                count = 1
                while num + 1 in s:
                    count += 1 
                    num = num + 1

                maxx = max(count, maxx)

        return maxx


        
        