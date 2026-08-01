class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        ind = {c: 0 for w in words for c in w}
        res = []

        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1]
            n = min(len(a), len(b))

            if len(a) > len(b) and a[:n] == b[:n]:
                return ""

            for j in range(n):
                if a[j] == b[j]:
                    continue
                if b[j] not in adj[a[j]]:
                    ind[b[j]] += 1
                    adj[a[j]].add(b[j])
                break

        q = deque([c for c in ind if ind[c] == 0])
        while q:
            c = q.popleft()
            res.append(c)
            
            for nei in adj[c]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)

        if len(res) != len(ind):
            return ""
        return "".join(res)                