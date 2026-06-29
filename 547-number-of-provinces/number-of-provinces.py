class Solution(object):

    
    def dfs1(self, g, s, visited, li):
        li.append(s)
        visited[s] = True
        
        
        for neighbor in g[s]:
            neighbor_idx = neighbor - 1
            if not visited[neighbor_idx]:
                self.dfs1(g, neighbor_idx, visited, li)

    def dfs(self, g):
        
        circle_count = 0
        visited = [False] * len(g)
        
        for i in range(len(g)):
            if not visited[i]:
                
                circle_count += 1
                la = []
                self.dfs1(g, i, visited, la)
                
        return circle_count

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
       
        converted = [[c + 1 for c in range(len(row)) if row[c] == 1] for row in isConnected]
        
        
        return self.dfs(converted)

