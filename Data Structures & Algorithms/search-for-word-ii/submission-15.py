class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # full word in path to mark complete word

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        found = set()
        tree = PrefixTree()
        for word in words:
            tree.insert(word)
        
        def dfs(node, r, c):
            if not (0 <= r < R and 0 <= c < C):
                return # out of bounds
            
            ch = board[r][c]
            if ch not in node.children:
                return # dead end

            if node.children[ch].word:
                found.add(node.children[ch].word)
            
            board[r][c] = '#' # otherwise clear temporarily to explore path
            dfs(node.children[ch], r, c - 1) # left
            dfs(node.children[ch], r, c + 1) # right
            dfs(node.children[ch], r - 1, c) # above
            dfs(node.children[ch], r + 1, c) # below
            board[r][c] = ch # return cell to original state

        for r in range(R):
            for c in range(C):
                dfs(tree.root, r, c)    

        return list(found)

        