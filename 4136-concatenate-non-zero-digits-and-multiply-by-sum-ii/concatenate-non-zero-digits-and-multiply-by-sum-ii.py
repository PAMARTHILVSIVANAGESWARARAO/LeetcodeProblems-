class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :type River: List[int]
        """
        MOD = 10**9 + 7
        m = len(s)
        
        # Precompute powers of 10 and their modular inverses
        pow10 = [1] * (m + 1)
        inv10 = [1] * (m + 1)
        
        # Modular inverse of 10 modulo 10^9 + 7 is 700000005
        INV_10 = pow(10, MOD - 2, MOD) 
        
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            inv10[i] = (inv10[i - 1] * INV_10) % MOD
            
        # Prefix arrays
        # pref_count[i] stores count of non-zero digits in s[0...i-1]
        # pref_sum[i] stores sum of non-zero digits in s[0...i-1]
        # pref_val[i] stores the positional prefix value sum up to s[0...i-1]
        pref_count = [0] * (m + 1)
        pref_sum = [0] * (m + 1)
        pref_val = [0] * (m + 1)
        
        for i in range(m):
            digit = int(s[i])
            
            # Carry forward previous states
            pref_count[i + 1] = pref_count[i]
            pref_sum[i + 1] = pref_sum[i]
            pref_val[i + 1] = pref_val[i]
            
            if digit != 0:
                pref_count[i + 1] += 1
                pref_sum[i + 1] += digit
                
                # Component value: digit * 10^(-current_non_zero_count)
                current_nz_count = pref_count[i + 1]
                term = (digit * inv10[current_nz_count]) % MOD
                pref_val[i + 1] = (pref_val[i] + term) % MOD
                
        ans = []
        for l, r in queries:
            # 1. Total non-zero elements in the range
            nz_in_range = pref_count[r + 1] - pref_count[l]
            
            if nz_in_range == 0:
                ans.append(0)
                continue
                
            # 2. Get the sum of digits in the range
            digit_sum = pref_sum[r + 1] - pref_sum[l]
            
            # 3. Calculate the concatenated number x
            # Extract raw factored prefix window: (pref_val[r+1] - pref_val[l])
            raw_val = (pref_val[r + 1] - pref_val[l]) % MOD
            
            # Scale it back up to its proper magnitude base: 10^(pref_count[r+1])
            # This sets the proper place value relative to the end index 'r'
            x = (raw_val * pow10[pref_count[r + 1]]) % MOD
            
            # 4. Compute final result for the query
            ans.append((x * digit_sum) % MOD)
            
        return ans
