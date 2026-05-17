class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while s and s[-1][0] < temperatures[i]:
                v, ix = s.pop()
                res[ix] = i - ix
            s.append((temperatures[i], i))
            
        return res


