class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)

        for c in s:
            if c1[c] != c2[c]:
                return False 

        return True


        