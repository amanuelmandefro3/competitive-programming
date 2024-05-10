# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_heap = []
        ans = 0
        for price in prices:
            # print(min_heap)    
            if min_heap and min_heap[0] < price:
                ans = max(ans, price-min_heap[0])
            heappush(min_heap, price)

        return ans        
        