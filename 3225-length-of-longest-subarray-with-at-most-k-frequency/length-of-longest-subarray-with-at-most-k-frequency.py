class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        r = 1
        left = 0
        freq = {}
        for right in range(n):
            c = nums[right]
            freq[c] = freq.get(c, 0) + 1
            # Decrease window length until k constraint is true again
            while freq[c] > k:
                d = nums[left]
                freq[d] -= 1
                left += 1
            r = max(r, right - left + 1)
        return r