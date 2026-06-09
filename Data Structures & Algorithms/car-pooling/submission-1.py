class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key = lambda x : x[1])
        min_heap = []
        total = 0
        for Npass, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                val = heapq.heappop(min_heap)[1]
                total -= val
               

            total += Npass
            if total > capacity:
                return False

            
            heapq.heappush(min_heap, (end,Npass))
        
        return True