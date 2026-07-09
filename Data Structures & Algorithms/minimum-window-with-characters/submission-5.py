class Solution:
    def minWindow(self, s: str, t: str) -> str:
        goal, curr = Counter(t), defaultdict(int)
        need, have = len(goal.keys()), 0
        l = 0 # start of window
        min_len = float('inf') 
        res = ''

        for r, ch in enumerate(s):
            curr[ch] += 1 # account for current chat
            if ch in goal and curr[ch] == goal[ch]:
                have += 1 # update if one more char achieved

                while have == need: # while qualifying, reduce window
                    cur_len = r - l + 1
                    if cur_len < min_len: # update if smaller
                        min_len = cur_len
                        res = s[l:r+1]
                    curr[s[l]] -= 1 # then reduce window from the left
                    if s[l] in goal and curr[s[l]] < goal[s[l]]:
                        have -= 1 # and reduce from have if disqualified
                    l += 1 # don't forget to update the window start

        return res
                    