class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() 
        curr = [] 
        result = [] 

        def dfs(start, curr):
            if sum(curr) == target:
                result.append(curr.copy())         
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue 
                if sum(curr) + candidates[i] <= target:
                    curr.append(candidates[i])
                    dfs(i + 1, curr)
                    curr.pop() 
        dfs(0, curr)
        return result
                
        