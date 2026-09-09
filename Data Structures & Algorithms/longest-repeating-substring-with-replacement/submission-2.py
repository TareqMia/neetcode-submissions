class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {} 
        result = 0
        left = 0 

        for right in range(len(s)):
            c = s[right]
            count[c] = 1 + count.get(c, 0)

            while left < len(s) and right - left + 1 - max(count.values()) > k:
                if (s[left]) in count:
                    count[s[left]] -= 1
                left += 1 

            result = max(result, right - left + 1)


        return result






        