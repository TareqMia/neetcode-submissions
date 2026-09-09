class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0 


        left = 0 
        right = 1

        while right < len(prices):

            if prices[left] > prices[right]:
                left = right 

            else:
                maxP = max(maxP, prices[right] - prices[left])

            right += 1

        return maxP
        
        

        
            
        
        