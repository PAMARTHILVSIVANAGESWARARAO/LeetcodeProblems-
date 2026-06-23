class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        M = r - l + 1
        
        # Base case for length 2:
        # dp0[j] stores ways ending at j with an increase (so previous was smaller: j - 1 choices)
        # dp1[j] stores ways ending at j with a decrease (so previous was larger: M - j choices)
        dp0 = [j - 1 for j in range(M + 1)]
        dp1 = [M - j for j in range(M + 1)]
        
        # Iterate for lengths from 3 up to n
        for _ in range(3, n + 1):
            next_dp0 = [0] * (M + 1)
            next_dp1 = [0] * (M + 1)
            
            # Prefix sum for dp1 to optimize the sum of dp1[k] for k < j
            pref_dp1 = 0
            for j in range(1, M + 1):
                next_dp0[j] = pref_dp1
                pref_dp1 = (pref_dp1 + dp1[j]) % MOD
                
            # Suffix sum for dp0 to optimize the sum of dp0[k] for k > j
            suff_dp0 = 0
            for j in range(M, 0, -1):
                next_dp1[j] = suff_dp0
                suff_dp0 = (suff_dp0 + dp0[j]) % MOD
                
            dp0 = next_dp0
            dp1 = next_dp1
            
        # The total number of valid zigzag arrays of length n
        ans = (sum(dp0) + sum(dp1)) % MOD
        return ans