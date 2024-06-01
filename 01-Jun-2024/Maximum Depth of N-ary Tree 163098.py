# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        queue = deque()
        if root:
            queue.append(root)
        ans = 0    
        while queue:
            ans += 1
            n = len(queue)

            for _ in range(n):
                curr = queue.popleft()
                if curr.children:
                    for ngb in curr.children:
                        queue.append(ngb)

        return ans                
        