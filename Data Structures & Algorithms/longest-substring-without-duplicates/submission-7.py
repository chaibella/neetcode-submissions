class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} # ch -> lastSeenIdx
        longest = 0
        l = 0 # start of window

        for r, c in enumerate(s):
            if c in seen and seen[c] >= l:
                l = seen[c] + 1
            else:
                longest = max(longest, r - l + 1)
            seen[c] = r

        return longest