class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def helper(left, right):
            if right >= left:
                mid = (left + right) // 2 

                if nums[mid] == target:
                    return mid 

                elif nums[mid] > target:
                    return helper(left, mid - 1) 

                elif nums[mid] < target:
                   return helper(mid + 1, right)

            else:
                return -1


        

        
        return helper(0, len(nums) - 1) 
        