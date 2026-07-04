class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int[] prev = new int[n];
        int[] curr = new int[n];

        // Initialize prev with the last row of the triangle
        for (int i = 0; i < n; i++) {
            prev[i] = triangle.get(n - 1).get(i);
        }

        // Bottom-up DP from second-last row to top
        for (int i = n - 2; i >= 0; i--) {
            for (int j = i; j >= 0; j--) {
                int down = triangle.get(i).get(j) + prev[j];
                int diagonal = triangle.get(i).get(j) + prev[j + 1];
                curr[j] = Math.min(down, diagonal);
            }
            // Clone current row to prev
            prev = curr.clone();
        }

        return prev[0];
        
    }
}