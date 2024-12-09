class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = {}
        for row in grid:
            row_str = ",".join(map(str,row))
            row_counts[row_str] = row_counts.get(row_str, 0) + 1
            
        count = 0
        n = len(grid)
        
        for col_idx in range(n):
            col_str = ",".join(str(grid[row_idx][col_idx]) for row_idx in range(n))
            count += row_counts.get(col_str, 0)
            
        return count
        