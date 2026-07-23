class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        R, C = len(heights), len(heights[0])
        pq, aq = deque(), deque()

        for r in range(R):
            pq.append((r, 0)) # left to pacific
            aq.append((r, C - 1)) # right to atlantic
        for c in range(1, C):
            pq.append((0, c)) # top excluding leftmost to pacific
        for c in range(C - 1):
            aq.append((R - 1, c)) # bottom excluding rightmost to atlantic

        def bfs(q):
            reaches = set()
            while q:
                r, c = q.popleft()
                reaches.add((r, c))
                
                for nr, nc in [(r,c-1), (r,c+1), (r-1,c), (r+1,c)]:
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue # off land
                    if (nr, nc) in reaches:
                        continue # already visited
                    if heights[nr][nc] < heights[r][c]:
                        continue # could not reach ocean because lower height

                    q.append((nr, nc)) # can reach, add to queue for processing
            return reaches

        pac, atl = bfs(pq), bfs(aq)
        lands = list(pac.intersection(atl))
        return [list(land) for land in lands]
