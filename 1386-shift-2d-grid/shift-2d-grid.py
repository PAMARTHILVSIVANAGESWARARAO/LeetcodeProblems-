class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # Get dimensions
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        # Optimize k to prevent redundant full rotations
        k = k % total_elements
        
        # Flatten the 2D grid into a 1D list
        flat = []
        for row in grid:
            flat.extend(row)
            
        # Rotate the 1D list to the right by k positions
        # The last k elements move to the front, followed by the rest
        shifted_flat = flat[-k:] + flat[:-k]
        
        # Reshape the 1D list back into the original m x n 2D grid
        result = []
        for i in range(0, total_elements, n):
            result.append(shifted_flat[i : i + n])
            
        return result
