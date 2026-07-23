class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, ocean):
            if (r, c) in ocean:
                return # already visited
            
            ocean.add((r, c)) # mark land as visited

            for nr, nc in [(r,c-1), (r,c+1), (r-1,c), (r+1,c)]:
                if (0 <= nr < R and 0 <= nc < C # within land
                    and heights[nr][nc] >= heights[r][c]): # water flowable
                    dfs(nr, nc, ocean)

        for r in range(R):
            dfs(r, 0, pac) # first column into pacific
            dfs(r, C - 1, atl) # last column into atlantic

        for c in range(1, C):
            dfs(0, c, pac) # first row from 2nd column into pacific
        
        for c in range(C - 1):
            dfs(R - 1, c, atl) # last row up to 2nd last column into atlantic


        return list(pac.intersection(atl))
