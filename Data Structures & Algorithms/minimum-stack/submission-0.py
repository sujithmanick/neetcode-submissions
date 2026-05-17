class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        _min = float("inf")
        if not self.stack:
            return "null"
        for i in range(len(self.stack)-1, -1, -1):
            _min = min(_min, self.stack[i])
        return _min
        
