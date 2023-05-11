class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        def dfs(sr,sc,original,color):
            if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or (not image[sr][sc] == original):
                return
            image[sr][sc] = color
            
            dfs(sr+1,sc,original,color)
            dfs(sr-1,sc,original,color)
            dfs(sr,sc+1,original,color)
            dfs(sr,sc-1,original,color)
        
        dfs(sr,sc,image[sr][sc],color)
        
        return image
        
