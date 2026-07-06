class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        remaining_count = 0
        current_max_end = 0
        
        for _, end in intervals:
            # If the current end extends past the max end seen, it is not covered
            if end > current_max_end:
                remaining_count += 1
                current_max_end = end
                
        return remaining_count