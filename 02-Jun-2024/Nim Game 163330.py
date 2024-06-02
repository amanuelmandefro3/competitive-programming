# Problem: Nim Game - https://leetcode.com/problems/nim-game/

class Solution:
    def canWinNim(self, n: int) -> bool:
        if not n % 4:
            return False
        return True
        