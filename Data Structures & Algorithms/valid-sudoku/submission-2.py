class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        row_col = [[ [] for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row[i]\
                    or  board[i][j] in col[j]\
                    or (board[i][j] in row_col[i//3][j//3]):
                        return False
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
                    row_col[i//3][j//3].append(board[i][j])
                
        return True


