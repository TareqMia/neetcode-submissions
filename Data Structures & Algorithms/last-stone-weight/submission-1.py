class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            if len(stones) >= 2:
                # heaviest = stones.pop() 
                # secondHeaviest = stones.pop()
                heaviest = -heapq.heappop(stones)
                secondHeaviest = -heapq.heappop(stones)

                if heaviest > secondHeaviest:
                    heapq.heappush(stones, -(heaviest - secondHeaviest))
                    # stones.append(heaviest - secondHeaviest)

                # stones.sort() 

        return -stones[0] if stones else 0