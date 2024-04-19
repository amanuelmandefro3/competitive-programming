# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        queue = deque() 
 
        for course in range(numCourses):
            if course not in indegree:
                queue.append(course)
           
        while queue:
            curr_node = queue.popleft()
            ans.append(curr_node)
            for ngb in graph[curr_node]:
                indegree[ngb] -= 1
                if indegree[ngb] == 0:
                    queue.append(ngb)

        return ans if len(ans) == numCourses else []    
            


        