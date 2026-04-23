class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = {}
        
        for i, num in enumerate(nums):
            if num not in pos:
                pos[num] = []
            pos[num].append(i)
        
        ans = [0] * len(nums)
        
        for indexes in pos.values():
            n = len(indexes)
            prefix = [0] * (n + 1)
            
            for i in range(n):
                prefix[i + 1] = prefix[i] + indexes[i]
            
            for i in range(n):
                left = i * indexes[i] - prefix[i]
                right = (prefix[n] - prefix[i + 1]) - (n - i - 1) * indexes[i]
                ans[indexes[i]] = left + right
        
        return ans