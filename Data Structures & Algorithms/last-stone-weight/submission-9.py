
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        nums = []
        for i in stones:
            heapq.heappush(nums, -i)
        
        while len(nums) > 1:
            x = heapq.heappop(nums)
            y =heapq.heappop(nums)

            heapq.heappush( nums, x - y)
        return abs(nums[0]) if nums else 0
