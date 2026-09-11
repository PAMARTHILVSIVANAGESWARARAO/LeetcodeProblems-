class Solution {

    public static int[] CountofZerosAndOnes(String s) {
        

        int zeroCount = 0;
        int oneCount = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '0') {
                zeroCount++;

            } else {
                oneCount++;

            }
        }
        return new int[] { zeroCount, oneCount };

    }

    public static boolean isValid(String s) {

        int balance = 0;

        for (int i = 0; i < s.length(); i++) {

            if (s.charAt(i) == '1') {
                balance++;
            } else {
                balance--;
            }

            if (balance < 0) {
                return false;
            }
        }

        return balance == 0;
    }

    public static ArrayList<String> getBrackets(int n) {
        int reqStringLength = n * 2;

        int totalCombinations = (int) Math.pow(2, reqStringLength);

        ArrayList<String> binaryStrings = new ArrayList<>();

        for (int i = 0; i < totalCombinations; i++) {
            String binary = Integer.toBinaryString(i);
            if (binary.length() == reqStringLength)
                binaryStrings.add(binary);
        }

        ArrayList<String> requiredStrings = new ArrayList<>();

        for (int i = 0; i < binaryStrings.size(); i++) {
            int zocount[] = CountofZerosAndOnes(binaryStrings.get(i));
            if (zocount[0] == n && zocount[1] == n) {

                if (isValid(binaryStrings.get(i))) {
                    requiredStrings.add(0, binaryStrings.get(i));
                }

            }
        }

        return requiredStrings;

    }



    public List<String> generateParenthesis(int n) {
        ArrayList<String> requiredStrings = getBrackets(n);

        ArrayList<String> res = new ArrayList<>();

        for (int i = 0; i < requiredStrings.size(); i++) {

            String binary = requiredStrings.get(i);
            String brackets = "";

            for (int j = 0; j < binary.length(); j++) {

                if (binary.charAt(j) == '1') {
                    brackets += "(";
                } else {
                    brackets += ")";
                }
            }

            res.add(brackets);
        }

        return res;

    }
}