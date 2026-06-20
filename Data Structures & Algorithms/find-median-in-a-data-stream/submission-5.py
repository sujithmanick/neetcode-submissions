from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heappush(self.small,  -1 * num)

        if (self.small and self.large and -1 * self.small[0] > self.large[0]):
            val = -1 * heappop(self.small)
            heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = heappop(self.small)
            heappush(self.large, -1 * val)

        if len(self.large) >  len(self.small) + 1:
            val = -1 * heappop(self.large)
            heappush(self.small,  val)
            
        

    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        if len(self.small) < len(self.large):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2
        
        