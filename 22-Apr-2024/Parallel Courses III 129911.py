# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        _min_time = 0
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for prevCourse, nextCourse in relations:
            graph[prevCourse].append(nextCourse)
            indegree[nextCourse] += 1
        queue = deque()    
        for i in range(n):
            if not indegree[i+1]:
                queue.append((i+1, time[i]))
        max_time = [0 for _ in  range(n)]        
        while queue:
            curr, curr_time = queue.popleft()
            _min_time = max(_min_time, curr_time)

            for ngb in graph[curr]:
                indegree[ngb] -= 1
                max_time[ngb-1] = max(max_time[ngb-1], curr_time)
                if indegree[ngb] == 0:
                    queue.append((ngb, max_time[ngb-1]+time[ngb-1])) 

        return _min_time                          

        