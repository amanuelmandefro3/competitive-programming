# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        m = m+n
        need = mean*m- sum(rolls)
        if need / n < 1 or need /n > 6:
            return []
        ans = [need//n]*n
        left = need - sum(ans)
        i = 0
        while left:
            ans[i] += 1
            left -= 1
            i += 1
        return ans        
        