class Solution {
    private static final int MOD = 1_000_000_007;

    public int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1;
        if (m <= 1) return 0;
        
        int size = 2 * m;
        long[][] T = new long[size][size];
        
        // Build transition matrix
        // State encoding: 
        // 0 to m-1 -> value i with UP direction
        // m to 2m-1 -> value i with DOWN direction
        for (int j = 0; j < m; j++) {
            // From (j, UP) to (k, DOWN) where k < j
            for (int k = 0; k < j; k++) {
                T[m + k][j] = 1;
            }
            // From (j, DOWN) to (k, UP) where k > j
            for (int k = j + 1; k < m; k++) {
                T[k][m + j] = 1;
            }
        }
        
        // Initial state vector for n = 2
        long[] F = new long[size];
        for (int k = 0; k < m; k++) {
            F[k] = k;          // ways to reach k via an UP move (elements < k)
            F[m + k] = m - 1 - k;  // ways to reach k via a DOWN move (elements > k)
        }
        
        // Power for matrix exponentiation: we need n - 2 transitions from n = 2
        long power = n - 2;
        long[][] Tn = matrixPower(T, power, size);
        
        // Multiply Tn * F to get final state counts
        long totalWays = 0;
        for (int i = 0; i < size; i++) {
            long ways = 0;
            for (int j = 0; j < size; j++) {
                ways = (ways + Tn[i][j] * F[j]) % MOD;
            }
            totalWays = (totalWays + ways) % MOD;
        }
        
        return (int) totalWays;
    }
    
    private long[][] matrixPower(long[][] base, long exp, int size) {
        long[][] res = new long[size][size];
        for (int i = 0; i < size; i++) {
            res[i][i] = 1;
        }
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = multiply(res, base, size);
            }
            base = multiply(base, base, size);
            exp >>= 1;
        }
        return res;
    }
    
    private long[][] multiply(long[][] A, long[][] B, int size) {
        long[][] C = new long[size][size];
        for (int i = 0; i < size; i++) {
            for (int k = 0; k < size; k++) {
                if (A[i][k] == 0) continue;
                for (int j = 0; j < size; j++) {
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
                }
            }
        }
        return C;
    }
}