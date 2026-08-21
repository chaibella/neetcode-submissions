class Solution:
    def minWindow(self, s: str, t: str) -> str:
        curr, goal = defaultdict(int), Counter(t)
        have, need = 0, len(goal.keys())
        min_len, res = float('inf'), ''
        l = 0 # window start

        for r, ch in enumerate(s):
            curr[s[r]] += 1
            if s[r] in goal and curr[s[r]] == goal[s[r]]:
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