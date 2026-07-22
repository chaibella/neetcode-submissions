class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


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
        trie = PrefixTree()
        for word in words:
            trie.insert(word)
        root = trie.root

        R, C = len(board), len(board[0])
        res = set()

        def dfs(r, c, node):
            if not (0 <= r < R and 0 <= c < C):
                return # out of bounds
            if board[r][c] not in node.children:
                return # dead end
            
            ch = board[r][c]
            nxt = node.children[ch]
            if nxt.word:
                res.add(nxt.word)
            
            board[r][c] = '#'
            dfs(r, c - 1, nxt)
            dfs(r, c + 1, nxt)
            dfs(r - 1, c, nxt)
            dfs(r + 1, c, nxt)
            board[r][c] = ch

        for r in range(R):
            for c in range(C):
                dfs(r, c, root)
        
        return list(res)











        