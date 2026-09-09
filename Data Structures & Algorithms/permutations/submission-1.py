class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = [] 
        curr = []


        def backtrack(curr):
            if len(curr) == len(nums):
                result.append(curr.copy()) 

            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtrack(curr) 
                    curr.pop() 


        backtrack([])
        return result
        