import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, num)

    def findMedian(self) -> float:
        _len = len(self.min_heap)
        self.min_heap.sort()
        mid = _len // 2
        if _len % 2 == 1:
            return self.min_heap[mid]
        else:
            return (self.min_heap[mid -1] + self.min_heap[mid]) / 2

        