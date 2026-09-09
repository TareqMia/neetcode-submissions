class Solution:
    def jump(self, nums: List[int]) -> int:

        # do a BFS on the array, seeing what is the max boundaries for the jump
        left = 0 
        right = 0 

        result = 0 

        while right < len(nums) - 1:
            farthest = 0 
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            left = right + 1 
            right = farthest 

            result += 1

        return result
        