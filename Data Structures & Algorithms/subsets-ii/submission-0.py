class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        result = []
        curr = []

        def backtrack(i):

            
            result.append(curr.copy()) 
                

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue 

                curr.append(nums[j])
                backtrack(j + 1)
                curr.pop()


        backtrack(0)
        return result


        