# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        ans = 0
        queue = deque()
        if root:
            queue.append(root)
        
        while queue:
            ans += 1
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                if curr.children:
                    for ngb in curr.children:
                        queue.append(ngb)
        
        return ans
