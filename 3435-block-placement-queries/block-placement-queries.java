import java.util.*;

class Solution {

    static class Fenwick {
        int n;
        int[] bit;

        Fenwick(int n) {
            this.n = n;
            bit = new int[n + 2];
        }

        void update(int idx, int val) {
            while (idx <= n) {
                bit[idx] = Math.max(bit[idx], val);
                idx += idx & -idx;
            }
        }

        int query(int idx) {
            int res = 0;
            while (idx > 0) {
                res = Math.max(res, bit[idx]);
                idx -= idx & -idx;
            }
            return res;
        }
    }

    public List<Boolean> getResults(int[][] queries) {
        TreeSet<Integer> obstacles = new TreeSet<>();
        obstacles.add(0);

        int mx = 0;
        for (int[] q : queries) {
            mx = Math.max(mx, q[1]);
        }

        obstacles.add(mx + 1);

        for (int[] q : queries) {
            if (q[0] == 1) {
                obstacles.add(q[1]);
            }
        }

        Fenwick bit = new Fenwick(mx + 2);

        Integer prev = null;
        for (int x : obstacles) {
            if (prev != null) {
                bit.update(x, x - prev);
            }
            prev = x;
        }

        List<Boolean> ans = new ArrayList<>();

        for (int i = queries.length - 1; i >= 0; i--) {
            int[] q = queries[i];

            if (q[0] == 1) {
                int x = q[1];

                int l = obstacles.lower(x);
                int r = obstacles.higher(x);

                obstacles.remove(x);

                bit.update(r, r - l);
            } else {
                int x = q[1];
                int sz = q[2];

                Integer p = obstacles.floor(x);

                int best = Math.max(
                        bit.query(p),
                        x - p
                );

                ans.add(best >= sz);
            }
        }

        Collections.reverse(ans);
        return ans;
    }
}