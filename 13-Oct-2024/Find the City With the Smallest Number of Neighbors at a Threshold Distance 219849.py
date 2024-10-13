# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dijkstra(start):
            dist = [float('inf')] * n
            dist[start] = 0
            heap = [(0, start)]
            
            while heap:
                current_dist, u = heappop(heap)
                if current_dist > dist[u]:
                    continue
                
                for v, w in graph[u]:
                    new_dist = current_dist + w
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heappush(heap, (new_dist, v))

            cnt = 0
            for d in dist:
                if d <= distanceThreshold:
                    cnt += 1
            return cnt

        min_reachable = float('inf')
        result_city = -1
        
        for city in range(n):
            reachable = dijkstra(city)
            if reachable < min_reachable or (reachable == min_reachable and city > result_city):
                min_reachable = reachable
                result_city = city
        
        return result_city
