class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [ ['.' for i in range(n)] for i in range(n)]
        res = []

        def _issafe(i,j):
            
            for r in range(i):
                if board[r][j] == 'Q':
                    return False

            r, c = i - 1, j - 1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            r, c = i - 1, j + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            return True
        
        def dfs(i):
            if i >= n:
                path = []
                for m in board:
                    path.append("".join(m))
                res.append(path.copy())
                return

            for j in range(n):
                board[i][j] = 'Q'
                if _issafe(i,j):
                    dfs(i + 1)
                board[i][j] = '.'


        dfs(0)
        return res