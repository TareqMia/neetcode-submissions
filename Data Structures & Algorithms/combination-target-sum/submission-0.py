class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = [] 
        currCombination = []


        def backtrack(start, currCombinatin):

            if sum(currCombination) == target:
                result.append(currCombination.copy()) 


            for i in range(start, len(nums)):

                if nums[i] + sum(currCombination) <= target:
                    currCombination.append(nums[i])
                    backtrack(i, currCombination)
                    currCombination.pop() 


        backtrack(0, currCombination)
        return result
        