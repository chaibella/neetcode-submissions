class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # adjacency list: char -> [charsAfterIt]
        adj = defaultdict(set)
        # indegree: char -> numCharsBeforeIt
        ind = { c: 0 for w in words for c in w }

        # compare adjacent words and add differing chars to adj and ind
        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1]
            n = min(len(a), len(b))

            # if 2 words are otherwise same, longer one cannot precede shorter
            if len(a) > len(b) and a[:n] == b[:n]:
                return ""
            
            for j in range(n):
                if a[j] == b[j]:
                    continue # skip shared prefix
                # found mismatch but was it already logged
                if b[j] not in adj[a[j]]:
                    adj[a[j]].add(b[j])
                    ind[b[j]] += 1
                break # break on first mismatch, we identified the relevant order

        # process q with available chars (no chars before it)
        res = []
        q = deque([c for c in ind if ind[c] == 0])
        while q:
            c = q.popleft()
            res.append(c) # next available char to process

            for nei in adj[c]:
                ind[nei] -= 1 # neighbor requires 1 less char
                if ind[nei] == 0: # if required count reaches 0
                    q.append(nei) # add it to q for processing


        # if unable to order all chars, return emtpy
        if len(res) != len(ind):
            return ""

        # if able to order all cahrs, return as string
        return "".join(res)