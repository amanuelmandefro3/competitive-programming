# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        min_heap = [1]
        heapq.heapify(min_heap)
        ugly_nums = {1}
        
        while n > 1:
            curr_ugly = heapq.heappop(min_heap)
            if curr_ugly * 2 not in ugly_nums:
                heapq.heappush(min_heap, curr_ugly*2)
                ugly_nums.add(curr_ugly*2)
            if curr_ugly * 3 not in ugly_nums:
                heapq.heappush(min_heap, curr_ugly*3)
                ugly_nums.add(curr_ugly*3) 
            if curr_ugly * 5 not in ugly_nums:
                heapq.heappush(min_heap, curr_ugly*5)
                ugly_nums.add(curr_ugly*5) 
            n -= 1
        return min_heap[0]              
        