class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        currMax = float('-inf')
        currSum = 0
        
        
        for i in range(n):
            currSum += nums[i]
            currMax = max(currSum, currMax)
            if currSum < 0:
                currSum = 0
                
        return currMax
        