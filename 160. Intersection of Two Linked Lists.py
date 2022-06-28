
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = headA
        l2 = headB
        l3 = []
        
        while(l1):
            l3.append(l1)
            l1 = l1.next
        
        
        while(l2):
            if l2 in l3:
                return l2
            l2 = l2.next
        return None
        
        