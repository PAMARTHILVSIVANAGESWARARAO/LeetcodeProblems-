import java.util.*;

class Solution {
    public int longestValidSubstring(String word, List<String> forbidden) {
        // Step 1: Store forbidden words in a set for O(1) lookups
        Set<String> forbiddenSet = new HashSet<>(forbidden);
        
        int maxLen = 0;
        int l = 0;
        int n = word.length();
        
        // Step 2: Expand the right pointer of our sliding window
        for (int r = 0; r < n; r++) {
            // Check backward up to 10 characters from the current right pointer
            // We stop if we hit the left boundary 'l' or go back 10 steps
            for (int i = r; i >= Math.max(l, r - 9); i--) {
                String sub = word.substring(i, r + 1);
                
                if (forbiddenSet.contains(sub)) {
                    // If forbidden, the left pointer must jump past the start of this substring
                    l = i + 1;
                    break; // No need to check further left for this 'r'
                }
            }
            // Step 3: Update the maximum length found so far
            maxLen = Math.max(maxLen, r - l + 1);
        }
        
        return maxLen;
    }
}