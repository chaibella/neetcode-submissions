class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set) # beforeChar -> [afterChars]
        indegree = { c: 0 for w in words for c in w } # setup all chars
        res = []

        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1] # compare adjacent words
            n = min(len(a), len(b)) # take shared size

            # same word but longer cannot come before itself
            if len(a) > len(b) and a[:n] == b[:n]:
                return ""

            for j in range(n):
                if a[j] == b[j]:
                    continue # skip shared prefix
                
                # found mismatch, but is it the first time?
                if b[j] not in adj[a[j]]:
                    indegree[b[j]] += 1 # only count 1x per char
                    adj[a[j]].add(b[j])

                break

        q = deque([c for c in indegree if indegree[c] == 0]) # available
        while q:
            c = q.popleft()
            res.append(c) # next available char, in order

            for nei in adj[c]: # what chars follow this one?
                indegree[nei] -= 1
                if indegree[nei] == 0: # and if that char has no more before
                    q.append(nei) # add to queue as now available

        if len(indegree) != len(res):
            return "" # could not order all chars
        return "".join(res) # return order as string