class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, v in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= v:
                past_i,past_v  = stack.pop()
                max_area = max(max_area, past_v * (i - past_i))
                start = past_i
            stack.append([start,v])
        while stack:
            past_i,past_v  = stack.pop()
            max_area = max(max_area, past_v * (len(heights) - past_i))

        return max_area