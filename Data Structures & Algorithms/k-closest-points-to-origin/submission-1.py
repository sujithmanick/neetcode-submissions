import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == 1 and k == 1:
            return points
        
        heap = []
        res = []
        for i in points:
            x1, y1 = i[0], i[1]

            euclidean = (x1 * x1 + y1 * y1)
            heapq.heappush(heap, (euclidean, (x1,y1)))

        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res

