class Solution {
    public int firstUniqChar(String s) {

        LinkedHashMap<Character, Integer> freqMap = new LinkedHashMap<>();

        // Count frequency
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            freqMap.put(ch, freqMap.getOrDefault(ch, 0) + 1);
        }

        // Find first character whose frequency is 1
        for (int i = 0; i < s.length(); i++) {
            if (freqMap.get(s.charAt(i)) == 1) {
                return i;
            }
        }

        return -1;
    }
}