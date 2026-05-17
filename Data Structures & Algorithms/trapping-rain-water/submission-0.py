class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = []
        r_max = [0] * len(height)
        res = []
        max_l = 0
        max_r = 0
        for i in height:
            l_max.append(max_l)
            max_l = max(max_l, i)
        
        for i in range(len(height)-1,-1,-1):
            r_max[i] = max_r
            max_r = max(max_r, height[i])

        for i in range(len(height)):
            if min(l_max[i],r_max[i]) - height[i] >= 0:
                res.append(min(l_max[i],r_max[i]) - height[i])
            else:
                res.append(0)

        return sum(res)

        