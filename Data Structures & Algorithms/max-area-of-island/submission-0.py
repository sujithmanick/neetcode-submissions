class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        def find_nearby_islands(r, c, area):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or \
                grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            return 1 + find_nearby_islands(r + 1, c, area) +\
            find_nearby_islands(r - 1, c, area) +\
            find_nearby_islands(r, c + 1, area) +\
            find_nearby_islands(r, c - 1, area)

            

            


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(find_nearby_islands(r, c, 0), max_area)

        return max_area