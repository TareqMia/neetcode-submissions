class Solution:

    """
    - use hashmap to store the index 
    - check if calculated value is in the hashmap 
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [] 

        h = {} 

        for index, num in enumerate(nums):
            potential = target - num 

            if potential in h:
                return sorted([index, h[potential]])

            else:
                h[num] = index 

        return []