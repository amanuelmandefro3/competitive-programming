# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        efficiency_speed = [[efficiency[i], speed[i]] for i in range(n)]
        efficiency_speed.sort(reverse=True)

        min_heap = []
        ans = 0
        sum_speed = 0
        for eff, speed in efficiency_speed:
            sum_speed += speed
            heappush(min_heap, speed)

            if len(min_heap) >k:
                mn = heappop(min_heap)
                sum_speed -= mn
            ans = max(ans, sum_speed*eff)

        return ans %(10**9 + 7)       