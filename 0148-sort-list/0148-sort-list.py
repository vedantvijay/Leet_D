# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next
        sorted_head = sorted(head_list)
        temp = ListNode(0)
        current = temp
        for i in sorted_head:
            current.next = ListNode(i)
            current = current.next
        return temp.next
