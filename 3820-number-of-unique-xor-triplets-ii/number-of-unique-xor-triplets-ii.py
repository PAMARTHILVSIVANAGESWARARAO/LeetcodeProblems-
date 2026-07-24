class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        # Determine strict upper bounds based on array constraints
        max_val = max(nums)
        limit = 1
        while limit <= max_val:
            limit <<= 1
        limit <<= 1  # Safe buffer matching max_val << 1
        
        # Step 1: Find all valid unique pair XOR values
        pair_xor_exists = [False] * limit
        for a in nums:
            for b in nums:
                pair_xor_exists[a ^ b] = True
                
        # Step 2: Combine pairs with a 3rd element to find final unique triplets
        triplet_xor_exists = [0] * limit
        for pair_val in range(limit):
            if pair_xor_exists[pair_val]:
                for c in nums:
                    triplet_xor_exists[pair_val ^ c] = 1
                    
        # Step 3: Count and return the aggregate number of unique triplets
        return sum(triplet_xor_exists)
