class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        counts = defaultdict(int)
        longest = 0
        start = 0

        for end, ch in enumerate(s):
            counts[ch] += 1
            maxf = max(maxf, counts[ch])

            while (end - start + 1) - maxf > k:
                counts[s[start]] -= 1
                start += 1

            longest = max(longest, end - start + 1)

        return longest
