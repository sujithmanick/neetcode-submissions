class Solution:
    def isValid(self, s: str) -> bool:
        _map = {'{':'}', '[':']', '(':')' }
        stack = []
        for i in s:
            if i in _map.keys():
                stack.append(i)
            else:
                if stack:
                    last = stack.pop()
                else:
                    return False
                if _map[last] != i:
                    return False
        return len(stack) == 0
            