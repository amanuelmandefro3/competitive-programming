# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parents = list(range(n))
        parents[firstPerson] = 0
        meetings.sort(key=operator.itemgetter(2))
        prev_time, curr_met = 0, set()
 

        for a, b, time in meetings:
            if time != prev_time:
                prev_time = time
                self.reset_meeting(parents, curr_met)
            curr_met.add(a)
            curr_met.add(b)
            self.union(parents, a, b)
        self.reset_meeting(parents, curr_met)
        return [i for i, j in enumerate(parents) if not j]

    def reset_meeting(self, parents, curr_met):
        for i in curr_met:
            if self.find(parents, i):
                parents[i] = i
            else:
                parents[i] = 0   
        curr_met.clear()

    def union(self, parents, a, b):
        p_a = self.find(parents, a)
        p_b = self.find(parents, b)
        if p_a < p_b:
            parents[p_b] = p_a
        else:
            parents[p_a] = p_b
            

    def find(self, parents, a):
        while a != parents[a]:
            a = parents[a]
        return a

    