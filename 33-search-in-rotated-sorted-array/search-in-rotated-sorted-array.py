class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = -1 
        for i in range(len(nums)):
            if nums[i] == target:
                res = i 
                break
        return res 