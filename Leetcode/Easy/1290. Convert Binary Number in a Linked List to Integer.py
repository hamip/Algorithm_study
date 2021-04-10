# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/submissions/

# 1290. Convert Binary Number in a Linked List to Integer


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = ""

        cur = head
        while cur:
            num += str(cur.val)
            cur = cur.next
    
        return int(num, 2)
            
        #first traverse the list and access the values of the node
        #values into the string and covert to binary
