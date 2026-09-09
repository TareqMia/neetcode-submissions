class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def backtracking(currString, leftCount, rightCount):
            if len(currString) == 2 * n:
                answer.append(currString)
                return

            if leftCount < n:
                backtracking(currString + "(", leftCount + 1, rightCount)

            if leftCount > rightCount:
                backtracking(currString + ")", leftCount, rightCount + 1)

        backtracking("", 0, 0)
        return answer