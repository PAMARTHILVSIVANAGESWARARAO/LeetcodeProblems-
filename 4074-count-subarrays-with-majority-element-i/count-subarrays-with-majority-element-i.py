class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # Shift offset to handle negative prefix sums safely
        offset = n + 1 
        
        # Max possible index in Fenwick tree is n + offset
        bit = FenwickTree(2 * n + 2)
        
        # Initially, the prefix sum before any element is 0
        current_sum = 0
        bit.update(current_sum + offset, 1)
        
        total_subarrays = 0
        
        for num in nums:
            # Transform value: +1 if target, -1 otherwise
            current_sum += 1 if num == target else -1
            
            # Query how many previous prefix sums are strictly smaller than current_sum
            total_subarrays += bit.query(current_sum + offset - 1)
            
            # Add the current prefix sum to the Fenwick Tree
            bit.update(current_sum + offset, 1)
            
        return total_subarrays

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        
    def update(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
            
    def query(self, i):
        sum_val = 0
        while i > 0:
            sum_val += self.tree[i]
            i -= i & (-i)
        return sum_val