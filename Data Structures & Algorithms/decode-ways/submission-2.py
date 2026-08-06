class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = ([0] * N) + [1]
        
        for i in range(N - 1, -1, -1):
            if s[i] == "0":
                continue # no valid mapping to 0 or starting with 0
            
            dp[i] += dp[i + 1] # else there is at least 1-digit

            if (i < N -1 and
                (s[i] == "1" or s[i] == "2" and s[i + 1] <= "6")):
                dp[i] += dp[i + 2] # valid 2-digit mapping
            
        return dp[0] # all paths starting from the beginning
            
