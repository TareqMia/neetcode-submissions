class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            anagram = "".join(sorted([i for i in s]))
            groups[anagram].append(s) 
        return groups.values()
        