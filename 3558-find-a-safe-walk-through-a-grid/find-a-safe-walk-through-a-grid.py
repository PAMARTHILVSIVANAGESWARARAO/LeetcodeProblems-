from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        
        # Tracking the minimum health lost to reach each cell
        min_lost = [[float('inf')] * n for _ in range(m)]
        min_lost[0][0] = grid[0][0]
        
        queue = deque([(grid[0][0], 0, 0)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            current_lost, r, c = queue.popleft()
            
            if r == m - 1 and c == n - 1:
                return (health - current_lost) >= 1
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    next_lost = current_lost + grid[nr][nc]
                    
                    if next_lost < min_lost[nr][nc]:
                        min_lost[nr][nc] = next_lost
                        if grid[nr][nc] == 0:
                            queue.appendleft((next_lost, nr, nc))
                        else:
                            queue.append((next_lost, nr, nc))
                            
        return False
