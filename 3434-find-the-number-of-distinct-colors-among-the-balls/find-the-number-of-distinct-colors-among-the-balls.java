class Solution {
    public int[] queryResults(int limit, int[][] queries) {

        int[] result = new int[queries.length];

        // ball -> color
        HashMap<Integer, Integer> ballColor = new HashMap<>();

        // color -> number of balls having that color
        HashMap<Integer, Integer> colorFreq = new HashMap<>();

        int distinctColors = 0;

        for (int i = 0; i < queries.length; i++) {

            int ball = queries[i][0];
            int newColor = queries[i][1];

            // If ball already has a color
            if (ballColor.containsKey(ball)) {

                int oldColor = ballColor.get(ball);

                // Remove ball from old color
                colorFreq.put(oldColor, colorFreq.get(oldColor) - 1);

                // If no ball has old color anymore
                if (colorFreq.get(oldColor) == 0) {
                    colorFreq.remove(oldColor);
                    distinctColors--;
                }
            }

            // Assign new color to ball
            ballColor.put(ball, newColor);

            // Add ball to new color
            colorFreq.put(
                newColor,
                colorFreq.getOrDefault(newColor, 0) + 1
            );

            // If this is a new color
            if (colorFreq.get(newColor) == 1) {
                distinctColors++;
            }

            result[i] = distinctColors;
        }

        return result;
    }
}