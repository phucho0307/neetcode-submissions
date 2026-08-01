class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = collections.Counter(tasks)
        maxHeap = [-val for val in maxHeap.values()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0
        while maxHeap or queue:
            #increase time, put the most freq task into heap with its push back time
            time +=1
            if maxHeap:
                cnt = 1+heapq.heappop(maxHeap)
                if cnt:
                    queue.append([cnt, time+n])
            #if time meets one of the task in queue, push it back
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time
