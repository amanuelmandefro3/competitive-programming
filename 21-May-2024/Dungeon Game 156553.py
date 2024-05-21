# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        memo = {}

        def dp(i,j):
            if i == len(dungeon)-1 and j == len(dungeon[0]) -1:
                print(i,j)
                return max(0,0-dungeon[i][j])
            if i == len(dungeon) or j == len(dungeon[0]):
                return float('inf')
            if (i,j) not in memo:
                
                memo[(i,j)] = max(0, min(dp(i+1,j), dp(i,j+1)) - dungeon[i][j])
     
            return memo[(i,j)]

        return dp(0,0)+1             

        