class Solution:

    """
    - store a postfix and prefix of the products before 
    and after the number
    - at each step, multiply the current value by either 
    the prefix or postfix 
    - make sure to update the prefix and postfix products accordingly 
    
    
    """


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums) 

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix 
            prefix *= nums[i] 

        postfix = 1 
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix 
            postfix *= nums[i] 


        return result

        
        