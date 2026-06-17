class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lengths = [0] * n
        
        # Step 1: Forward pass to compute lengths
        curr_len = 0
        for i, char in enumerate(s):
            if char.islower():
                curr_len += 1
            elif char == '*':
                curr_len = max(0, curr_len - 1)
            elif char == '#':
                curr_len *= 2
            elif char == '%':
                pass
            lengths[i] = curr_len
            
        # If k is out of bounds of the final string
        if k >= curr_len or k < 0:
            return '.'
            
        # Step 2: Backward pass to track index k
        for i in range(n - 1, -1, -1):
            char = s[i]
            prev_len = lengths[i - 1] if i > 0 else 0
            
            if char.islower():
                if k == prev_len:
                    return char
                # If k < prev_len, k remains the same
            elif char == '*':
                # k remains the same because it's within the valid prefix length
                pass
            elif char == '#':
                if k >= prev_len:
                    k -= prev_len
            elif char == '%':
                k = prev_len - 1 - k
                
        return '.'