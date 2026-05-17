
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif self.min_stack[-1] >= val:
            self.min_stack.append(val)
        return None

        

    def pop(self) -> None:
        print(self.stack, self.min_stack if self.min_stack else "")
        val = self.stack.pop()

        if self.min_stack and self.min_stack[-1] == val:
            self.min_stack.pop()
            return val
        else:
            return None
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None