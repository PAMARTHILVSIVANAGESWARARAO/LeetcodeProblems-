class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
        StringBuilder result = new StringBuilder();
        
        for (String word : words) {
            long totalWeight = 0;
            
            // Step 1: Calculate total weight for the current word
            for (int i = 0; i < word.length(); i++) {
                int charIndex = word.charAt(i) - 'a';
                totalWeight += weights[charIndex];
            }
            
            // Step 2: Take total weight modulo 26
            int remainder = (int) (totalWeight % 26);
            
            // Step 3: Map using reverse alphabetical order (0 -> 'z', 1 -> 'y', ..., 25 -> 'a')
            char mappedChar = (char) ('z' - remainder);
            
            result.append(mappedChar);
        }
        
        return result.toString();
    }
}