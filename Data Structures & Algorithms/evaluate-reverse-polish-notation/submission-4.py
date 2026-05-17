class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        data = 0
        for i in tokens:
                
            if i == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(b+a)

            elif i == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif i == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(b*a)
            elif i == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(i))
        return stack[0]
