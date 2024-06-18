# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stones_position = set(stones)
        memo = {}

        def dp(curr_pos, k):
            if curr_pos == stones[-1]:
                return True
            if (curr_pos, k) in memo:
                return memo[(curr_pos, k)]
            if curr_pos not in stones_position:
                return False

            for step in range(k-1, k+2):
                if step > 0 and (curr_pos + step) in stones_position:
                    if dp(curr_pos + step, step):
                        memo[(curr_pos, k)] = True
                        return True

            memo[(curr_pos, k)] = False
            return False
        
        return dp(stones[0]+1, 1)