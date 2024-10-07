# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        n = len(start)
        l,r = 0, start[-1] - start[0] + d + 1


        def helper(score: int) -> bool:
            pre = start[0]
            for i in range(1, n):
                if start[i] + d - pre < score:
                    return False
                pre = max(start[i], pre + score)
            return True

        while l < r:
            mid = l + (r - l) // 2
            if helper(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1