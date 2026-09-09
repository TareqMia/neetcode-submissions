class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [] 

        anagrams = collections.defaultdict(list) 

        for word in strs:
            anagram = ''.join(sorted([c for c in word]))
            anagrams[anagram].append(word)

        return list(anagrams.values())

        