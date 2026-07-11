from collections import deque
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build the adjacency list representation of the graph
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_components_count = 0
        
        # Step 2: Traverse every unvisited vertex to find connected components
        for i in range(n):
            if not visited[i]:
                # Initialize BFS tracking variables
                queue = deque([i])
                visited[i] = True
                
                vertex_count = 0
                edge_count = 0
                
                # Step 3: Run BFS to map out the current component
                while queue:
                    curr = queue.popleft()
                    vertex_count += 1
                    # Accumulate degrees of all nodes in this component
                    edge_count += len(adj[curr])
                    
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                # Step 4: Validate if the component is complete
                # Each undirected edge is counted twice (once from each endpoint)
                if edge_count == vertex_count * (vertex_count - 1):
                    complete_components_count += 1
                    
        return complete_components_count
