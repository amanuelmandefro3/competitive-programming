# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_order, task_process = [], []
        ans, time = [0]*len(tasks), 1

        for i in range(len(tasks)):
            heappush(task_order, [tasks[i][0], tasks[i][1], i])

        i = 0
        while i < len(tasks):
            while len(task_order) > 0 and task_order[0][0] <= time:
                curr_task = heappop(task_order)
                heappush(task_process, [curr_task[1], curr_task[2], curr_task[0]])


            if len(task_process) == 0 and len(task_order) > 0:
                time = task_order[0][0]
            else:
                task = heappop(task_process)
                time += task[0]
                ans[i] = task[1]
                i += 1

        return ans            