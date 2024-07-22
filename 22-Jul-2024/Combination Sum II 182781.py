# Problem: Combination Sum II - https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        arr = []
        path = []
        
        num = candidates[0]
        num_count = candidates.count(num)
        path_count = defaultdict(int)
        if num_count == len(candidates):
            if sum(candidates) == target:
                return [candidates]
            elif sum(candidates) < target:     
                return []
        def backtrack(curr):
            if sum(path) == target:
                new_comb = path[:]
                # # new_comb.sort()
                # new_comb = tuple(new_comb)
                # # print(new_comb)
                if new_comb not in arr:
                    arr.append(new_comb)
                    # path_count[new_comb] = 1
                return 
            elif sum(path) > target:
                return
            last_pop = float('inf')    
            for i in range(curr, len(candidates)):
                if last_pop == candidates[i]:
                    continue
                path.append(candidates[i])
                backtrack(i+1)
                
                last_pop = path.pop()

        backtrack(0)
        return arr                
    