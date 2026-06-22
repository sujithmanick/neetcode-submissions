from collections import Counter, deque
from heapq import heapify, heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        max_heap = [ -val for _, val in count.items()]
        heapify(max_heap)
        q = deque([])
        
        time = 0

        while max_heap or q:
            time += 1

            if max_heap:
                val = 1 + heappop(max_heap)
                if val:
                    q.append([val, time + n])

            if q and q[0][1] == time:
                v, tme = q.popleft()
                heappush(max_heap, v)
        return time
