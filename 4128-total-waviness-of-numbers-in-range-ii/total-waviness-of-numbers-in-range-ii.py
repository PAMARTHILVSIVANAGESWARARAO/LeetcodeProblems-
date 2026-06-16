from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def solve(n: int) -> int:
            if n < 100:
                return 0
            
            s = str(n)
            length = len(s)
            
            @lru_cache(None)
            def dp(idx: int, prev: int, prev2: int, is_less: bool, is_started: bool) -> int:
                # Base case: completed constructing the number
                if idx == length:
                    return 0
                
                limit = 9 if is_less else int(s[idx])
                ans = 0
                
                for d in range(limit + 1):
                    next_is_less = is_less or (d < limit)
                    
                    if not is_started:
                        if d == 0:
                            # Still placing leading zeros
                            ans += dp(idx + 1, -1, -1, next_is_less, False)
                        else:
                            # Found the first significant digit
                            ans += dp(idx + 1, d, -1, next_is_less, True)
                    else:
                        # We have started. Check if the previous position (prev) becomes a peak/valley
                        waviness_contribution = 0
                        if prev2 != -1 and prev != -1:
                            if prev2 < prev > d:    # Peak
                                waviness_contribution = 1
                            elif prev2 > prev < d:  # Valley
                                waviness_contribution = 1
                        
                        # Count the contribution from this configuration
                        # ways = total valid numbers that can be formed from the next choices onwards
                        ans += dp(idx + 1, d, prev, next_is_less, True)
                        
                        # Add the waviness contribution of 'prev' for all valid suffixes formed from here
                        if waviness_contribution > 0:
                            ans += waviness_contribution * count_ways(idx + 1, next_is_less)
                            
                return ans

            @lru_cache(None)
            def count_ways(idx: int, is_less: bool) -> int:
                if idx == length:
                    return 1
                limit = 9 if is_less else int(s[idx])
                total_ways = 0
                for d in range(limit + 1):
                    total_ways += count_ways(idx + 1, is_less or (d < limit))
                return total_ways

            return dp(0, -1, -1, False, False)

        return solve(num2) - solve(num1 - 1)