class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

    
        for i in range(len(arr)):
            for j in range(len(arr)):
                # Ensure we are not matching the exact same element
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False
