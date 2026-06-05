class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits == "":
            return []
        char_set = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        char = []
        def dfs(i):
            if i >= len(digits):
                res.append("".join(char))
                return

            for k in range(len(char_set[digits[i]])):
                char.append(char_set[digits[i]][k])
                dfs(i + 1)
                char.pop()



        dfs(0)
        return res
