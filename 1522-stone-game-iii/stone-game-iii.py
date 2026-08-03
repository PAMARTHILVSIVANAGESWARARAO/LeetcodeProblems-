class Solution(object):
    def stoneGameIII(self, a):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        dp = [0, 0, 0]
        x = [0, 0]
        
        for v in reversed(a):
            r = max(v - dp[0], v + x[0] - dp[1], v + x[0] + x[1] - dp[2])
            x[1] = x[0]
            x[0] = v
            dp[2] = dp[1]
            dp[1] = dp[0]
            dp[0] = r

        clamped_val = max(-1, min(dp[0], 1))
        return ["Bob", "Tie", "Alice"][clamped_val + 1]
