class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 # or else will get division by 0 error
        right = max(piles) 
        result = right

        while left <= right: 
            hours = 0

            mid = (left + right) // 2  # k

            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                result = min(result, mid) 

                # change right pointer to see if lower value possible
                right = mid - 1 

            else:
                left = mid + 1

        return result

        