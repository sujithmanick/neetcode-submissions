class Solution:
    def trap(self, height: List[int]) -> int:
        lmax= height[0]
        rmax = height[len(height) - 1] 

        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            if height[l] <= height[r]:
                l += 1
                lmax = max(height[l], lmax)
                if min(lmax, rmax) - height[l] > 0:
                    res += min(lmax, rmax) - height[l]
               
            else:
                r -= 1
                rmax = max(height[r], rmax)
                if min(rmax, lmax) - height[r] > 0:
                    res += min(rmax, lmax) - height[r]
                
        return res

