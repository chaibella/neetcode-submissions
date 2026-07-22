class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, group):
            if not (0 <= r < R and 0 <= c < C):
                return # out of land
            group.add((r, c)) # mark land as reached

            # can others be reached
            for nr, nc in [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]:
                if (0 <= nr < R and 0 <= nc < C and 
                    heights[nr][nc] >= heights[r][c] and
                    (nr, nc) not in group):
                    dfs(nr, nc, group)


        for c in range(0, C): # top row
            dfs(0, c, pac)

        for r in range(1, R): # left column, minus already visited (0,0)
            dfs(r, 0, pac)

        for c in range(0, C): # bottom row
            dfs(R - 1, c, atl)

        for r in range(0, R - 1): # right column minus visited (R-1,C-1)
            dfs(r, C - 1, atl)

        return list(pac.intersection(atl))
