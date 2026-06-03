class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        state = []

        def backtrack(open_C, close_C):
            if open_C == close_C == n:
                res.append("".join(state))

            if open_C < n:
                state.append('(')
                backtrack(open_C + 1, close_C)
                state.pop()

            if close_C < n and open_C > close_C:
                state.append(')')
                backtrack(open_C, close_C + 1)
                state.pop()


        backtrack(0, 0)
        return res