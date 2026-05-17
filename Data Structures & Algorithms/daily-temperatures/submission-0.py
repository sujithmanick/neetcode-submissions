class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res =[0]*len(temperatures)
        stack =[]

        for i,val in enumerate(temperatures):
            print(stack)
            if stack and stack[-1][1] < val:
                while stack and stack[-1][1] < val:
                    ind, vl = stack.pop()
                    res[ind] = i - ind
                
            stack.append((i,val)) 

        return res