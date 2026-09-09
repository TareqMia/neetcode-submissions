class Solution:

    """
    - option 1: create 2 hasmaps and see if they are equal 
    - option 2: sort the char arrays for each string 
    and see if equal
    
    
    """

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        sCounter = collections.Counter(s)
        tCounter = collections.Counter(t)

        for i in range(len(s)):
            c = s[i]
            if sCounter[c] != tCounter[c]:
                return False 
                
        return True


        
        