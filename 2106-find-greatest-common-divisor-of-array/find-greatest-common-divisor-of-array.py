class Solution:
    def findGCD(self, nums: List[int]) -> int:
        import math 
        return math.gcd(max(nums) , min(nums))