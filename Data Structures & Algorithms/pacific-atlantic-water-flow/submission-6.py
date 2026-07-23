class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # check if empty
        if not heights or not heights[0]:
            return []

        # get dimensions and setup queues
        R, C = len(heights), len(heights[0])
        pac, atl = deque(), deque()

        # fill the queues with starter values
        for c in range(C):
            pac.append((0, c)) # add top row to pacific
            atl.append((R - 1, c)) # add bottom row to atlantic
        for r in range(1, R):
            pac.append((r, 0)) # add left, excluding top row, to pacific
        for r in range(R - 1):
            atl.append((r, C - 1)) # add right, excluding bottom row, to atlantic

        # setup bfs to process queue
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
                        continue # cannot flow from here, lower height
                    
                    q.append((nr, nc))
            return reaches

        # call the bfs on each queue
        pacific = bfs(pac)
        atlantic = bfs(atl)

        # return land that reaches both oceans as list
        return list(pacific.intersection(atlantic))