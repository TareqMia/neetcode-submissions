class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz' }

        if not digits:
            return []


        ans, sol = [], [] 

        def backtrack(i):

            if len(sol) == len(digits):
                ans.append("".join(sol))
                return 
            letters = m[digits[i]]
            for d in letters:
                sol.append(d)
                backtrack(i + 1)
                sol.pop() 

        backtrack(0)
        return ans

        