class Solution:
    def minWindow(self, s: str, t: str) -> str:
        goal, curr = Counter(t), defaultdict(int)
        have, need = 0, len(goal.keys())
        min_len = float('inf')
        res = ''
        l = 0 # window start

        for r, ch in enumerate(s):
            curr[ch] += 1
            if ch in goal and curr[ch] == goal[ch]:
                have += 1
                while have == need:
                    cur_len = r - l + 1
                    if cur_len < min_len:
                        min_len = cur_len
                        res = s[l:r + 1]
                    curr[s[l]] -= 1
                    if s[l] in goal and curr[s[l]] < goal[s[l]]:
                        have -= 1
                    l += 1

        return res
        