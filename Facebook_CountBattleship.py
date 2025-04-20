"""
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).
"""
"""
Visit each coordinate of the board and check if it is a battleship. If it is, check if it is part of a horizontal or vertical battleship. If it is, add all the coordinates of the battleship to a set to mark them as visited. Increment the count of battleships by 1 for each new battleship found.
Return the final count of battleships.
"""
from typing import List
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visited = set()
        count = 0
        m=len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                cords=[(i,j)]
                if (i,j) not in visited and board[i][j] == 'X':
                    #check if horizontal or vertical also to get complete co-ordinates of battleship
                    if i+2 < m and board[i+1][j] == board[i+2][j]=='X':
                        cords=[(i,j),(i+1, j), (i+2, j)]
                    elif j+2 <n and board[i][j+1] == board[i][j +2 ]=='X':
                        cords=[(i,j),(i, j+1), (i, j+2)]
                    for cord in cords:
                        visited.add(cord)
                    count +=1
        return count
s = Solution()
#print(s.countBattleships([["X", ".", "X"], [".", ".", "."], ["X", "X", "X"]])) # 3
print(s.countBattleships([ [".",  "."], ["X", "X"]])) # 2
        