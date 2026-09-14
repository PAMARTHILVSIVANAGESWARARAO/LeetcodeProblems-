import java.math.BigInteger;
import java.util.ArrayList;

class Solution {
    public int[] plusOne(int[] digits) {

        String actualNum = "";

        for (int x : digits)
            actualNum += x;

        BigInteger number = new BigInteger(actualNum).add(BigInteger.ONE);

        String arrNum = "" + number;

        ArrayList<Integer> al = new ArrayList<>();

        for (int i = 0; i < arrNum.length(); i++) {
            char num = arrNum.charAt(i);

            al.add(Integer.parseInt(String.valueOf(num)));
        }

        int res[] = new int[al.size()];

        for (int i = 0; i < al.size(); i++) {
            res[i] = al.get(i);
        }

        return res;
    }
}