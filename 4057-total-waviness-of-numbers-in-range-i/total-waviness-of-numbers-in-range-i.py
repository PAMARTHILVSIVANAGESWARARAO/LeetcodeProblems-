class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total_waviness = 0
        
        for num in range(num1, num2 + 1):
            s = str(num)
            # Numbers with fewer than 3 digits have a waviness of 0
            if len(s) < 3:
                continue
                
            # Iterate through the inner digits (excluding first and last)
            for i in range(1, len(s) - 1):
                prev_digit = s[i - 1]
                curr_digit = s[i]
                next_digit = s[i + 1]
                
                # Check for Peak
                if curr_digit > prev_digit and curr_digit > next_digit:
                    total_waviness += 1
                # Check for Valley
                elif curr_digit < prev_digit and curr_digit < next_digit:
                    total_waviness += 1
                    
        return total_waviness