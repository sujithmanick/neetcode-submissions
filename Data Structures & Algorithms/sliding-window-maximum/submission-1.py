class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        from collections import deque
        dq=deque()
        result = []
        _len = len(nums)

        while r < _len:
            
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)

            if dq[0] < l:
                dq.popleft()

            if (r-l+1) == k:
                result.append(nums[dq[0]])
                l+=1
            r+=1
        return result