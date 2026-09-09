class Solution:

    """
    - use a hashmap to store the sorted characters as the key, 
    and the value will be the words that fall into that category

    time: O(N * k log k)
    space: O(n)

    
    """


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            anagram = "".join(sorted([i for i in s]))
            groups[anagram].append(s) 
        return groups.values()
        