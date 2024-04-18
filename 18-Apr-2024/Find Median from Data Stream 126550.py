# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

        

    def addNum(self, num: int) -> None:
        total_length = len(self.max_heap) + len(self.min_heap) 
        if total_length%2 == 0:
            len_max_be = total_length//2
            if not self.min_heap:
                heapq.heappush(self.min_heap, num)

            elif self.min_heap and self.min_heap[0] < num:
                rem_val = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -rem_val)
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)

        else:
            if not self.max_heap:
                heapq.heappush(self.min_heap, num)
            elif -self.max_heap[0] > num:
                rem_val = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -rem_val)
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num) 
        # print(self.min_heap, self.max_heap)               


    def findMedian(self) -> float:
        total_length = len(self.min_heap) + len(self.max_heap)
        if total_length % 2:
            return self.min_heap[0]
        first = heapq.heappop(self.min_heap)
        second = self.min_heap[0]
        heapq.heappush(self.min_heap, first)
            
        return (first + second)/2    
        


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()