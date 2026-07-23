class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # check if empty
        if not heights or not heights[0]:
            return

        # setup dimensions and queues
        R, C = len(heights), len(heights[0])
        pac, atl = deque(), deque()

        # fill queues
        for r in range(R):
            pac.append((r, 0)) # add left to pacific
            atl.append((r, C - 1)) # add right to atlantic
        for c in range(1, C):
            pac.append((0, c)) # add top excluding leftmost to pacific
        for c in range(C - 1):
            atl.append((R - 1, c)) # add bottom excluding rightmost to atlantic

        # setup bfs to process input queue
        def bfs(q):
            # collect land that water reaches
            reaches = set()
            # collect while land remaining in queue
            while q:
                # mark next land as reached
                r, c = q.popleft()
                reaches.add((r, c))
                # check all 4 directions outbound from this land
                for nr, nc in [(r,c-1), (r,c+1), (r-1,c), (r+1,c)]:
                    # check that it is still inland
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    # check that is hasn't been marked already as reachable
                    if (nr, nc) in reaches:
                        continue
                    # check that it actually is reachable - higher ground
                    if heights[nr][nc] < heights[r][c]:
                        continue
                   # if all true, then add to queue for processing
                    q.append((nr, nc))
            # return collected land that water reaches
            return reaches

        # call bfs on/from both oceans
        pacific, atlantic = bfs(pac), bfs(atl)

        # return land that reaches both oceans
        lands = list(pacific.intersection(atlantic))
        return [list(land) for land in lands]