class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = [] 
        queue = deque() 

        left = 0 
        right = 0 

        while right < len(nums):

            # check if the curr value is greater than what is in the
            # queue already 
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop() 
            queue.append(right)

            # check if the value at the left index still in window 
            if left > queue[0]:
                queue.popleft() 

            if right + 1 >= k:
                result.append(nums[queue[0]])
                left += 1

            right += 1

        return result
        