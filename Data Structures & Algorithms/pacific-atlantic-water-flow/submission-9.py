class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        R, C = len(heights), len(heights[0])
        pac, atl = deque(), deque()

        for r in range(R):
            pac.append((r, 0)) # left to pac
            atl.append((r, C - 1)) # right to atl
        for c in range(1, C):
            pac.append((0, c)) # top excluding leftmost to pac
        for c in range(C - 1):
            atl.append((R - 1, c)) # bottom excluding rightmost to atl

        def bfs(q):
            reaches = set()
            while q:
                r, c = q.popleft()
                reaches.add((r, c))
                for nr, nc in [(r,c-1), (r,c+1), (r-1,c), (r+1,c)]:
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue # offland
                    if (nr, nc) in reaches:
                        continue # already visited
                    if heights[nr][nc] < heights[r][c]:
                        continue # cannot reach
                    q.append((nr, nc))

            return reaches

        lands = list(bfs(pac).intersection(bfs(atl)))
        return [list(land) for land in lands]
                    






