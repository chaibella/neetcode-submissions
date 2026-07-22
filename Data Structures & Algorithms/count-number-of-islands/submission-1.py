class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if not (0 <= r < R and 0 <= c < C):
                return # out of bounds
            if not grid[r][c] == '1':
                return # no more land
            
            grid[r][c] = '0' # sink island

            dfs(r, c - 1) # left
            dfs(r, c + 1) # right
            dfs(r - 1, c) # above
            dfs(r + 1, c) # below
            return # completed checking 4 directionally


        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        
        return islands