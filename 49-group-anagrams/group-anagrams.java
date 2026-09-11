import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Arrays;

class Solution {
    public static String sortString(String s) {
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        return new String(arr);
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagramMap = new HashMap<>();

        for (String x : strs) {
            String sortedKey = sortString(x);
            
            
            if (!anagramMap.containsKey(sortedKey)) {
                anagramMap.put(sortedKey, new ArrayList<>());
            }
            
            anagramMap.get(sortedKey).add(x);
        }

       
        return new ArrayList<>(anagramMap.values());
    }
}
