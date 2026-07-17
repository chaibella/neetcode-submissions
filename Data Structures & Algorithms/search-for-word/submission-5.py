class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def dfs(i, r, c):
            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            
            tmp = board[r][c]
            board[r][c] = '#'
            
            for nr, nc in [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]:
                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                if board[nr][nc] == '#':
                    continue

                if dfs(i + 1, nr, nc):
                    board[r][c] = tmp
                    return True
            
            board[r][c] = tmp
            return False


        for r in range(R):
            for c in range(C):
                if dfs(0, r, c):
                    return True
        return False