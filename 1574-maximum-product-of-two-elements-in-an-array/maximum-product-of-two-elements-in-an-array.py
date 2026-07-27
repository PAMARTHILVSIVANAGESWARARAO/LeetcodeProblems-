class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)

        e1 = nums[-1] - 1
        e2 = nums[-2] - 1

        return e1*e2