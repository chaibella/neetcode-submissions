class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i == len(s):
                memo[i] = 1
            elif s[i] == "0":
                memo[i] = 0
            else:
                count = dfs(i + 1)
                if (i < len(s) - 1 and
                    (s[i] == "1" or 
                     s[i] == "2" and s[i + 1] <= "6")):
                    count += dfs(i + 2)
                memo[i] = count
            
            return memo[i]
        
        return dfs(0)

