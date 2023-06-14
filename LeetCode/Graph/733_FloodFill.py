"""
Question
https://leetcode.com/problems/flood-fill/
"""

#Approach
"""
--> Do BFS to traverse thorugh all the pixels with same color as the starting pixel
--> DFS also works here

"""

#Code
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r, c = len(image), len(image[0])
        q = collections.deque([])
        rows = [-1, 1, 0, 0]
        cols = [0, 0, 1, -1]

        def isSafe(row, col):
            if row < 0 or col < 0 or row >= r or col >= c:
                return False
            return True

        if(image[sr][sc] == color):
            return image
        
        replaceColor = image[sr][sc]

        q.append((sr, sc))

        while q:
            row, col = q.popleft()
            image[row][col] = color
            for dx, dy in zip(rows, cols):
                if(isSafe(row+dx, col+dy) and image[row+dx][col+dy] == replaceColor):
                    q.append((row+dx, col+dy))
        return image
