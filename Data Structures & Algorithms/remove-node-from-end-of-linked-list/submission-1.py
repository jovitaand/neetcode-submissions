# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #count from the end of the list and remove the nth number
        dummy = ListNode(0, head) #to keep the copy of the list
        left = dummy
        right  = head
        #position right
        while n > 0 and right:
            right = right.next
            n -= 1
        #position left
        while right:
            left = left.next
            right = right.next

        #delete: just update the pointers
        left.next = left.next.next
        return dummy.next