class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def dfs(i, r, c):
            if board[r][c] != word[i]: # not the next char
                return False
            if i == len(word) - 1: # made it to the end
                return True
            
            tmp = board[r][c]
            board[r][c] = '#' # mark as visited

            for nr, nc in [(r,c-1), (r,c+1), (r-1,c), (r+1,c)]:
                if not (0 <= nr < R and 0 <= nc < C):
                    continue # out of bounds, skip
                if dfs(i + 1, nr, nc): # if found path
                    board[r][c] = tmp # restore cell value before returning True
                    return True 


            board[r][c] = tmp # restore cell value before returning False
            return False
            

        for r in range(R): # word may start from any cell
            for c in range(C):
                if dfs(0, r, c): # if found, exit
                    return True
        return False # not found