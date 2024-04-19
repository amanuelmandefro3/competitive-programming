# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # meetings = []
        # min_heap = []
        # for start, end in meetings:
        #     heapq.heappush(min_heap, (start, end))
        # meetings = min_heap
        # print(min_heap)    
        heapq.heapify(meetings)
        rooms = defaultdict(int)
        mn_heap = []
        room = 0
        print(meetings)

        room_heap = [i for i in range(n)]    
        while room_heap and meetings:
            start, end =  heapq.heappop(meetings)
            while mn_heap and mn_heap[0][0] <= start:
                end_room =  heapq.heappop(mn_heap) 
                heapq.heappush(room_heap, end_room[1])
            room = heapq.heappop(room_heap)
            rooms[room] += 1
            heapq.heappush(mn_heap, (end, room))   
            
              

            # rooms[room] += 1
            # heapq.heappush(mn_heap, (end, room))
            # room += 1
        while meetings:
            start, end = heapq.heappop(meetings)
            while mn_heap and mn_heap[0][0] <= start:
                end_room =  heapq.heappop(mn_heap) 
                heapq.heappush(room_heap, end_room[1])
            if room_heap:
                room = heapq.heappop(room_heap)
                heapq.heappush(mn_heap, (end, room))
                rooms[room] += 1
            else:        
                previous_end, room = heapq.heappop(mn_heap)
                if previous_end > start:
                    end += previous_end - start
                heapq.heappush(mn_heap, (end, room))
                rooms[room] += 1

        _max_held_room = 0
        print(rooms)
        for i in range(1,n):
            if rooms[i] > rooms[_max_held_room]:
                _max_held_room  = i
        return _max_held_room           



        