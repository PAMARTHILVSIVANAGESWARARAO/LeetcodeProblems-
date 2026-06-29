from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_count = 0
        minutes = 0
        
        # Step 1: Scan grid for starting conditions
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        # Multi-source BFS traversal
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue and fresh_count > 0:
            minutes += 1
            # Process all currently rotten oranges for this minute level
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # If neighbor is within bounds and is a fresh orange
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Turn it rotten
                        fresh_count -= 1  # Decrement fresh count
                        queue.append((nr, nc))
                        
        # Step 3: Check if any fresh oranges are left unreachable
        return minutes if fresh_count == 0 else -1
