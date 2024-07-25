# Problem: Reach a Number - https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        possible_moves, move = 0, 0
      
        while possible_moves < target or ( possible_moves - target) % 2 != 0:
            move += 1
            possible_moves += move


        return move
        