# https://leetcode.com/problems/middle-of-the-linked-list/submissions/

# 876. Middle of the Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# two - pointer approach

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # when fast reaches null or fast.next reaches null, slow pointer is at middle
        return slow
