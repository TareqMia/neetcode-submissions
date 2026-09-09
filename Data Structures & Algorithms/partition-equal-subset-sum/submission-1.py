class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        - see if we can get to sum(nums) // 2 
        - for each num, subtract from the target, and see if 
        we can reach the new target
        """

        if sum(nums) % 2:
            return False 

        dp = set() 
        target = sum(nums) // 2
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            newDp = set() 

            for num in dp:
                total = num + nums[i]
                if total == target:
                    return True
                newDp.add(total)
                newDp.add(num)
            dp = newDp

        return True if target in dp else False


        
        