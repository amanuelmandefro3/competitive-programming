# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sum_head = ListNode()
        curr_point = sum_head
        curr = head.next
        curr_sum = 0

        while curr:
            if curr.val == 0:
                curr_point.next = ListNode(curr_sum)
                curr_sum = 0
                curr_point = curr_point.next
            else:
                curr_sum += curr.val
            curr = curr.next

        return sum_head.next            
                        