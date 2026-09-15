import java.math.BigInteger;

class Solution {
    public String addBinary(String a, String b) {
        // 1. Convert both binary strings to BigInteger
        BigInteger num1 = new BigInteger(a, 2);
        BigInteger num2 = new BigInteger(b, 2);
        
        // 2. Add them together
        BigInteger sum = num1.add(num2);
        
        // 3. Convert the sum back to a binary string
        return sum.toString(2);
    }
}
