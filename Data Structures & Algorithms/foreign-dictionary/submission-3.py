class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set) # char -> [comesAfterChar]
        indegree = { c: 0 for w in words for c in w } # numCharsBefore
        res = []

        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1] # compare adjacent words
            n = min(len(a), len(b)) # take min or shared size
            
            if len(a) > len(b) and a[:n] == b[:n]:
                return "" # after word cannot be shorter while starting with before word
            
            for j in range(n):
                if a[j] == b[j]:
                    continue # skip shared prefix
                
                # found mismatch, but is it the first time
                if b[j] not in adj[a[j]]:
                    indegree[b[j]] += 1 # don't count same char twice
                    adj[a[j]].add(b[j])
                break # break as soon as mismatch, first or not

        q = deque([c for c in indegree if indegree[c] == 0]) # no chars before these
        while q: # process every char that is/becomes available (no char before it)
            c = q.popleft()
            res.append(c)
            for nei in adj[c]: # what chars come after this one?
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei) # add to queue if no more chars before it

        if len(res) < len(indegree): # couldn't order all chars
            return ""
        return "".join(res)


