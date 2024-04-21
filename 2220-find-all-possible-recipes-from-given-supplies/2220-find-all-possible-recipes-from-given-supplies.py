class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        dependency = defaultdict(list)
        indegree = defaultdict(int)
        ans, n = [], len(recipes)

        for i in range(n):
            for ing in ingredients[i]:
                dependency[ing].append(recipes[i])
                indegree[recipes[i]] += 1
        recipes = set(recipes)

        queue = deque(supplies)
        while queue:
            node = queue.popleft()
            if node in recipes:
                ans.append(node)
            for ngb in dependency[node]:
                indegree[ngb] -= 1
                if indegree[ngb] == 0:
                    queue.append(ngb)
        return ans                


            
        