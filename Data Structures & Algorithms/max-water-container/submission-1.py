class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        storage_ = float("-inf")
        while l < r:
            storage_ = max((r-l) * min(height[l], height[r]), storage_)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return storage_
