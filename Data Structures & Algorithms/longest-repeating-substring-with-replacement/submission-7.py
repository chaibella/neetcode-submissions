class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int) # ch -> count
        longest = 0 
        l = 0
        maxf = 0

        for r, c in enumerate(s):
            counts[c] += 1
            maxf = max(maxf, counts[c])
            if (r - l + 1) - maxf > k:
                counts[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        
        return longest