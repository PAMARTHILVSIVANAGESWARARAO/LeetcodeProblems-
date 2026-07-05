class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        
        # dp[r][c] stores [max_score, paths_count]
        # Initialize with -1 score to represent unreachable states
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        
        # Base case: Starting position 'S' at the bottom-right
        dp[n-1][n-1] = [0, 1]
        
        # Iterate backwards from bottom to top, right to left
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                # Skip obstacles and the starting cell processing itself
                if board[r][c] == 'X' or (r == n - 1 and c == n - 1):
                    continue
                
                max_prev_score = -1
                total_paths = 0
                
                # Check three incoming directions: down, right, down-right
                for dr, dc in [(1, 0), (0, 1), (1, 1)]:
                    nr, nc = r + dr, c + dc
                    
                    # Ensure neighbor is inside the grid boundary
                    if nr < n and nc < n and dp[nr][nc][0] != -1:
                        prev_score, prev_paths = dp[nr][nc]
                        
                        if prev_score > max_prev_score:
                            max_prev_score = prev_score
                            total_paths = prev_paths
                        elif prev_score == max_prev_score:
                            total_paths = (total_paths + prev_paths) % MOD
                
                # If at least one valid path reaches this cell
                if max_prev_score != -1:
                    # 'E' counts as 0 points, numbers add their integer value
                    current_val = 0 if board[r][c] == 'E' else int(board[r][c])
                    dp[r][c] = [max_prev_score + current_val, total_paths]
        
        # Return results at top-left corner 'E'
        final_score, final_paths = dp[0][0]
        return [final_score if final_score != -1 else 0, final_paths]
