class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort() 

        while len(stones) > 1:
            if len(stones) >= 2:
                heaviest = stones.pop() 
                secondHeaviest = stones.pop() 

                if heaviest > secondHeaviest:
                    stones.append(heaviest - secondHeaviest)

                stones.sort() 

        return stones[0] if stones else 0