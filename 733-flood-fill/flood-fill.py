class Solution:
    def dfs(self , img, x, y, oldColor, newColor):
        if (x < 0 or x >= len(img) or
            y < 0 or y >= len(img[0]) or
            img[x][y] != oldColor):
            return

        img[x][y] = newColor

        self.dfs(img, x + 1, y, oldColor, newColor)
        self.dfs(img, x - 1, y, oldColor, newColor)
        self.dfs(img, x, y + 1, oldColor, newColor)
        self.dfs(img, x, y - 1, oldColor, newColor)


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color:
            return image

        
        oldColor = image[sr][sc]
        self.dfs(image, sr, sc, oldColor, color)

        return image