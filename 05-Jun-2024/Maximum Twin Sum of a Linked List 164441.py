# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
           
        prev.next = None
         
        rev_head = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = rev_head
            rev_head = curr
            curr = next_node

        max_sum = head.val + rev_head.val
        head, rev_head = head.next, rev_head.next    
        while head and rev_head:
            max_sum = max(max_sum, head.val + rev_head.val) 
            head, rev_head = head.next, rev_head.next

        return max_sum       