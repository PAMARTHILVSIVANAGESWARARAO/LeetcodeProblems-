class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zc = oc = tc = 0
        for x in nums:
            if x == 1:
                oc += 1
            elif x == 2:
                tc += 1
            else:
                zc += 1
        
        
        nums[:] = [0] * zc + [1] * oc + [2] * tc
