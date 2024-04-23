# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] *= -1
        heapq.heapify(piles)    
        for _ in range(k):
            _max = heapq.heappop(piles)
            heapq.heappush(piles, floor(_max/2))
   
        return sum(piles)*-1                   
            