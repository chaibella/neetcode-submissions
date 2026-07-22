class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # completed word string to mark end of word

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
        
        def dfs(r, c, node):
            if not (0 <= r < R and 0 <= c < C):
                return # out of bounds
            
            ch = board[r][c]
            if ch not in node.children:
                return # dead end

            nxt = node.children[ch]
            if nxt.word:
                found.add(nxt.word) # found a word, continue exploring beyond

            board[r][c] = '#' # mark while exploring to not read again
            dfs(r, c - 1, nxt) # left
            dfs(r, c + 1, nxt) # right
            dfs(r - 1, c, nxt) # above
            dfs(r + 1, c, nxt) # below
            board[r][c] = ch # restore char after done exploring

        
        # search for words, explore tree, starting from every cell
        for r in range(R):
            for c in range(C):
                dfs(r, c, tree.root)
        
        return list(found)


            

