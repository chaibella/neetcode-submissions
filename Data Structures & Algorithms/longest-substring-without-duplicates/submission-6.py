class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {} # ch -> lastIdx
        longest = 0
        start = 0

        for end, ch in enumerate(s):
            if ch in last and last[ch] >= start:
                start = last[ch] + 1
            else:
                longest = max(longest, end - start + 1)
            last[ch] = end

        return longest
        
