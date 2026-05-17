from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        sub_boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == '.':
                    continue
                tuple_key = tuple([row//3, col//3])
                if value in row_set[row] or value in col_set[col] or value in sub_boxes[tuple_key]:
                    return False

                row_set[row].add(value)
                col_set[col].add(value)
                sub_boxes[tuple_key].add(value)

        return True
