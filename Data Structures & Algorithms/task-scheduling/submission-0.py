class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        """
        - use a heap and a queue 
        - heap will store the counts for each task, making sure we take the most frequent one 
        - queue will store the taks for the cooldown 
        - keep track of time, when cooldown time is reached for elem in front of queue, 
        add it back to the heap
        """

        freq = collections.Counter(tasks)
        heap = [-c for c in freq.values()]

        heapq.heapify(heap)
        queue = collections.deque() 
        time = 0 

        while queue or heap:
            time += 1 

            if heap:
                count = heapq.heappop(heap)
                count += 1 

                if count:
                    queue.append([count, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

        return time
             



        