# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        l2_list = []
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next
        res1 = "".join(str(i) for i in l1_list[::-1])
        res2 = "".join(str(i) for i in l2_list[::-1])
        sumi = int(res1) + int(res2)
        rev_sumi = str(sumi)[::-1]
        head = ListNode(0)
        current = head
        for char in rev_sumi:
            current.next = ListNode(int(char))
            current = current.next

        return head.next
