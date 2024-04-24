# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        dependency = [set() for _ in range(numCourses)]
        indegree = defaultdict(int)
        for a, b in prerequisites:
            graph[a].add(b)
            indegree[b] += 1

        queue = deque()
        for course in range(numCourses):
            if not indegree[course]:
                queue.append(course)
        print(queue)
        while queue:
            course = queue.popleft()
            for ngb in graph[course]:
                dependency[ngb].update(dependency[course])
                dependency[ngb].add(course)
                indegree[ngb] -= 1
                if indegree[ngb] == 0:
                    queue.append(ngb)
        print(dependency)            
        ans = []
        for u, v in queries:
            ans.append(u in dependency[v])

        return ans          

        