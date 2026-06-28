class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        
        # Step 2: The first element must be 1
        arr[0] = 1
        
        # Step 3: Iterate through the array and enforce the maximum allowable step of 1
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)
            
        # The last element will hold the maximum possible value
        return arr[-1]
        