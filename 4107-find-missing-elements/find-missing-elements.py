class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        n = nums[-1]
        m = nums[0]

        res = []

        for i in range(m , n):
            if i not in nums:
                res.append(i)

        return res 
