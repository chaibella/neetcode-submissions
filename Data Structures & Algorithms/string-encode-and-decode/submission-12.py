class Solution:

    def encode(self, strs: List[str]) -> str:
        vals = []
        for s in strs:
            vals.append(f"{len(s)}#{s}")
        return ''.join(vals)

    def decode(self, s: str) -> List[str]:
        vals = []
        i, N = 0, len(s)
        
        while i < N:
            size = ''
            while i < N and s[i].isdigit():
                size += s[i]
                i += 1
            start = i + 1 # skip the hash #
            end = i + 1 + int(size)
            vals.append(s[start:end])
            i = end
        return vals

