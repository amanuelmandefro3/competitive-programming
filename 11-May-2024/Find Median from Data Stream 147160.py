# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
    def balanceHeaps(self):
        if len(self.min_heap) + 1 < len(self.max_heap) :
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))   
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
 

    def addNum(self, num: int) -> None:
        if not self.max_heap or self.max_heap[0] <= -num:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)    

        self.balanceHeaps()              


    def findMedian(self) -> float:
        total_length = len(self.min_heap) + len(self.max_heap)
        if total_length % 2:
            return -self.max_heap[0]
        
            
        return (-self.max_heap[0] + self.min_heap[0])/2    
        


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()