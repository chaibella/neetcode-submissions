class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int) # char -> countInWIndow
        longest = 0
        start = 0
        max_count = 0

        for end, ch in enumerate(s):
            counts[ch] += 1
            max_count = max(max_count, counts[ch])
            while (end - start + 1) - max_count > k:
                counts[s[start]] -= 1
                start += 1
            longest = max(longest, end - start + 1)

        return longest
