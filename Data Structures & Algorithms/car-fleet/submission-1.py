class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in sorted(list(zip(position, speed)), key = lambda x:x[0], reverse=True):
            pos, speed = i
            time = (target - pos) / speed
            if stack and time <= stack[-1]:
                continue
            
            stack.append(time)
        return len(stack)