class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        component = [0] * n
        current_id = 0
        
        for i in range(1, n):
            # If the gap between sorted adjacent elements is too large, break the component
            if nums[i] - nums[i - 1] > maxDiff:
                current_id += 1
            component[i] = current_id
            
        # Step 2: Answer each query in O(1) time
        ans = []
        for u, v in queries:
            ans.append(component[u] == component[v])
            
        return ans