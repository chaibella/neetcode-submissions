class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set) # char -> [followingChars]
        indegrees = { c: 0 for w in words for c in w } # precedingChars
        res = []

        for i in range(len(words) - 1):
            one, two = words[i], words[i + 1] # compare adjacent words
            sm = min(len(one), len(two))
            if len(one) > len(two) and one[:sm] == two[:sm]:
                return "" # shared prefix, no mismatching char
            
            for j in range(sm):
                if one[j] == two[j]:
                    continue # skip shared prefix
                if two[j] not in adj[one[j]]: # if not yet added
                    adj[one[j]].add(two[j]) # one[j] -> two[j]
                    indegrees[two[j]] += 1 # two[j] needs how many before it
                break # found mismatching char to determing direction

        q = deque([c for c in indegrees if indegrees[c] == 0]) # no preceding
        while q:
            c = q.popleft() # next char with no chars preceding itself
            res.append(c)

            for nei in adj[c]: # this char comes before what other chars
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)

        if len(res) != len(indegrees): # not all letters could be ordered
            return ""
        return "".join(res) # otherwise we ordered every char 
                

