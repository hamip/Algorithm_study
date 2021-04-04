# https://leetcode.com/problems/palindrome-number/

# 9. Palindrome Number

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        
        # fast runner moves two nodes while slow runner moves one
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        # when the number of node is odd, skip the middle node for proper palindrome check
        if fast:
            slow = slow.next
            
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
            
        # if comparison is properly finished, slow and reverse will both be None
        return not rev
      
      
