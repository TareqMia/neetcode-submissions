class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []  


        for index, num in enumerate(nums):
            if index > 0 and nums[index - 1] == nums[index]:
                continue 

            left = index + 1
            right = len(nums) - 1

            while left < right:
                candidate = nums[left] + nums[right] + num 

                if candidate > 0:
                    right -= 1
                elif candidate < 0:
                    left += 1

                else:
                    result.append([nums[left], nums[right], num])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result 

        