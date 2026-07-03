import java.util.*;

class Solution {
    private List<int[]>[] adj;
    private boolean[] online;
    private long[] memo;
    private final long INF = Long.MAX_VALUE / 2;

    public int findMaxPathScore(int[][] edges, boolean[] online, long k) {
        int n = online.length;
        this.online = online;
        
        // Step 1: Build the adjacency list
        adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        
        // Collect unique edge costs for binary search
        TreeSet<Integer> uniqueCosts = new TreeSet<>();
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int cost = edge[2];
            adj[u].add(new int[]{v, cost});
            uniqueCosts.add(cost);
        }
        
        // Convert to an array for index-based binary searching
        List<Integer> costList = new ArrayList<>(uniqueCosts);
        
        int low = 0;
        int high = costList.size() - 1;
        int ans = -1;
        
        // Step 2: Binary Search over the possible minimum edge costs
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int targetMinCost = costList.get(mid);
            
            // Reset memoization array for each check
            memo = new long[n];
            Arrays.fill(memo, -1);
            
            if (dfs(0, n - 1, targetMinCost) <= k) {
                ans = targetMinCost; // This threshold is valid, try a larger one
                low = mid + 1;
            } else {
                high = mid - 1; // Too restrictive, try a lower threshold
            }
        }
        
        return ans;
    }
    
    private long dfs(int u, int target, int minEdgeCost) {
        if (u == target) {
            return 0;
        }
        if (memo[u] != -1) {
            return memo[u];
        }
        
        long minTotalCost = INF;
        
        for (int[] edge : adj[u]) {
            int v = edge[0];
            int weight = edge[1];
            
            // Only traverse if edge weight satisfies the threshold and the next node is online
            if (weight >= minEdgeCost && online[v]) {
                long nextCost = dfs(v, target, minEdgeCost);
                if (nextCost != INF) {
                    minTotalCost = Math.min(minTotalCost, weight + nextCost);
                }
            }
        }
        
        return memo[u] = minTotalCost;
    }
}