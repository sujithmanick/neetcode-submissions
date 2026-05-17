class Solution:
    def isValid(self, s: str) -> bool:
        hash_dict = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        stack = []

        for _ in s:
            if _ not in ['[','{','(']:
                if stack:
                    pair = stack.pop()
                    if hash_dict[_] != pair:
                        return False
                else:
                    return False
                continue
            stack.append(_)
        return True if not stack else False
