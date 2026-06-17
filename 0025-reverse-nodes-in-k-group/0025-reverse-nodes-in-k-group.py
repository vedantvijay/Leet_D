# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        result = []
        i = 0 
        m = k
        while i < len(res):
            if (len(res[i:m])==k):
                result += res[i:m][::-1]
            else:
                result += res[i:m]
            m = m+k
            i = i+k
        
        temp = ListNode(0)
        current = temp
        for val in result:
            current.next = ListNode(val)
            current = current.next
        return temp.next