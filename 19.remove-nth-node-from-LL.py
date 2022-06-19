# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow = head
        fast = head
        for i in range(0,n):
            fast = fast.next
        
        if(fast):
            while(fast.next):
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next
        else: 
            head = head.next
        
        return head
        
            
        