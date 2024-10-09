# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v, w in times:
            graph[u].append((v,w))

    
        times = {node:float('inf') for node in range(1,n+1)}
        times[k] = 0
        processed = set()

        heap = [(0, k)]
    
    
        while heap:
            cost, curr = heappop(heap)
            if curr in processed:
                continue
            processed.add(curr)

            for ngb, weight in graph[curr]:
                time = cost + weight
                if time < times[ngb]:
                    times[ngb] = time
                    heappush(heap, (time, ngb))
        mn_time = 0
        for node, time in times.items():
            if time == float('inf'):
                return -1
            mn_time = max(mn_time, time)    

        return mn_time


        