class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word: # check for each char in path
            if ch not in cur.children: # add if not yet added
                cur.children[ch] = TrieNode()
            cur = cur.children[ch] # move to that child
        cur.end = True # mark that node ends valid word


    def search(self, word: str) -> bool:
        
        def dfs(node, i):
            if i == len(word): # reached the end of the word
                return node.end # return boolean if complete word
            
            ch = word[i]
            if ch != '.': # if a specific char
                if ch not in node.children: # and does not exist in path
                    return False # then word does not exist in dictionary
                return dfs(node.children[ch], i + 1) # else check next char in path
            else: # or it is a wildcard, so skip current letter and check remainder
                for child in node.children.values(): # check the nodes not the char
                    if dfs(child, i + 1):
                        return True # return early if path found complete
                return False # otherwise didnt find word ultimately
        
        return dfs(self.root, 0) # start call on root and first char of word
            
            
        
