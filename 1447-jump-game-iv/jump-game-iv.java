import java.util.*;

class Solution {
    public int minJumps(int[] arr) {

        int n = arr.length;

        if (n == 1) {
            return 0;
        }

        HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();

        for (int i = 0; i < n; i++) {

            map.putIfAbsent(arr[i], new ArrayList<>());

            map.get(arr[i]).add(i);
        }

        Queue<Integer> queue = new LinkedList<>();

        boolean[] visited = new boolean[n];

        queue.offer(0);

        visited[0] = true;

        int steps = 0;

        while (!queue.isEmpty()) {

            int size = queue.size();

            while (size-- > 0) {

                int current = queue.poll();

                if (current == n - 1) {
                    return steps;
                }

                if (current - 1 >= 0 && !visited[current - 1]) {

                    visited[current - 1] = true;

                    queue.offer(current - 1);
                }

                if (current + 1 < n && !visited[current + 1]) {

                    visited[current + 1] = true;

                    queue.offer(current + 1);
                }

                ArrayList<Integer> sameValues = map.get(arr[current]);

                if (sameValues != null) {

                    for (int index : sameValues) {

                        if (!visited[index]) {

                            visited[index] = true;

                            queue.offer(index);
                        }
                    }

                    map.remove(arr[current]);
                }
            }

            steps++;
        }

        return -1;
    }
}