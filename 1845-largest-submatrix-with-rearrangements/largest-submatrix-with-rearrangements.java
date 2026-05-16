import java.util.*;

class Solution {
    public int largestSubmatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        int[][] height = new int[m][n];

        for (int j = 0; j < n; j++) {
            height[0][j] = matrix[0][j];
        }

        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 1) {
                    height[i][j] = height[i - 1][j] + 1;
                }
            }
        }

        int max = 0;

        for (int i = 0; i < m; i++) {
            int[] arr = height[i].clone();

            Arrays.sort(arr);

            for (int j = n - 1; j >= 0; j--) {
                int width = n - j;
                int area = arr[j] * width;

                max = Math.max(max, area);
            }
        }

        return max;
    }
}