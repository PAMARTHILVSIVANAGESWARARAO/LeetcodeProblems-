class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Convert to a set to make "if i not in nums" instant (O(1) time instead of O(N))
        num_set = set(nums)
        l = []
        
        # We only ever need to check from 1 up to len(nums) + 1
        limit = len(nums) + 1
        
        for i in range(1, limit + 1):
            if i not in num_set:   
                l.append(i) # Append 'i' (the missing number), not nums[i]
        
        l = sorted(l)
        return l[0] # Return the smallest missing positive found