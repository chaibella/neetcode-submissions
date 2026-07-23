class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, ocean):
            ocean.add((r, c)) # add land as reached

            for nr, nc in [(r,c-1), (r,c+1), (r-1,c), (r+1,c)]:
                if ((0 <= nr < R and 0 <= nc < C) # still land
                    and (nr, nc) not in ocean # not processed
                    and heights[nr][nc] >= heights[r][c]): # water flows
                    dfs(nr, nc, ocean)

        # reverse water flow from pacific, top-left
        for c in range(C):
            dfs(0, c, pac) # top row
        for r in range(1, R):
            dfs(r, 0, pac) # left column, excluding column at first row

        # reverse water flow from atlantic, bottom-right
        for c in range(C):
            dfs(R - 1, c, atl) # bottom row
        for r in range(R - 1):
            dfs(r, C - 1, atl) # right column, excluding column at last row

        return list(pac.intersection(atl))