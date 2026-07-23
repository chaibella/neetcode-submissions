class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, group):
            # mark land as visited
            group.add((r, c))

            # check relevant neighbors
            for nr, nc in [(r,c-1), (r,c+1), (r-1,c), (r+1,c)]:
                if ((0 <= nr < R and 0 <= nc < C) # still land
                    and (nr, nc) not in group # not previously visited
                    and heights[nr][nc] >= heights[r][c]): # reachable, reversed
                    dfs(nr, nc, group)

        # land reachable from pacific (top, left)
        for c in range(C): # every cell on top row
            dfs(0, c, pac)
        for r in range(1, R): # from 2nd to last cell in left column
            dfs(r, 0, pac)

        # land reachable from atlantic (bottom, right)
        for c in range(C): # every cell in bottom row
            dfs(R - 1, c, atl)
        for r in range(0, R - 1): # up to the 2nd to last cell in right column
            dfs(r, C - 1, atl)

        return list(pac.intersection(atl))