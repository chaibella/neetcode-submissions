class Solution:
    def minWindow(self, s: str, t: str) -> str:
        goal, curr = Counter(t), defaultdict(int)
        need, have = len(goal.keys()), 0
        l = 0 # window start
        res = ''
        min_len = float('inf') # we want smallest window

        for r, ch in enumerate(s):
            curr[ch] += 1 # first add current char
            # and if current char unlocks new char, update
            # but ONLY the first time, as we can have more than needed
            if ch in goal and curr[ch] == goal[ch]:
                have += 1

                # then while this is the case, try to get min size 
                # where we still qualify - decrease window from left
                while have == need:
                    cur_len = r - l + 1
                    if cur_len < min_len: # add if smaller
                        min_len = cur_len
                        res = s[l:r+1]
                    # then shorten the window from the left*
                    curr[s[l]] -= 1
                    # and if by doing we lose a needed char, update
                    if s[l] in goal and curr[s[l]] < goal[s[l]]:
                        have -= 1
                    l += 1 # and just make sure to actually update window

        return res







