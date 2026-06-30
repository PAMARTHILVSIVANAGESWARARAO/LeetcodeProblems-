from collections import deque
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
       
        n = len(rooms)
        

        visited = set([0])
        
        
        queue = deque([0])
        
        while queue:
           
            current_room = queue.popleft()
            
            
            for key in rooms[current_room]:
                
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
                    
        
        return len(visited) == n