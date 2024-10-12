# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        queue=deque()
        queue.append(root)

        def dfs(node1, node2):
            if not node2:
                return True
            if not node1 or node1.val != node2.val:
                return False
            return dfs(node1.right, node2.next) or dfs(node1.left, node2.next)

        while(queue):
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.val == head.val and dfs(curr, head):
                    return True
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
        return False
        