import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        min_ = 9999999999999

        while l <= r:
            k = (l + r) // 2

            total = 0
            for p in piles:
                total += math.ceil(p / k)
            
            if total <= h:
                min_ = k
                r = k - 1
            else:
                l = k + 1
        return min_
            
