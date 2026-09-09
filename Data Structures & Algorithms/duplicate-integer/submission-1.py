class Solution:

    """
    - check to see if the set from nums is less than the length
    of nums
    - alternatively, we can sort nums and check if any adjacent 
    numbers are equal

    """


    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


    
         