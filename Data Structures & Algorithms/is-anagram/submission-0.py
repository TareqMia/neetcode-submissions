class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        sCounter = collections.Counter(s)
        tCounter = collections.Counter(t)

        for i in range(len(s)):
            c = s[i]
            if sCounter[c] != tCounter[c]:
                return False 

            else:
                sCounter[c] -= 1
                tCounter[c] -= 1

        return True


        
        