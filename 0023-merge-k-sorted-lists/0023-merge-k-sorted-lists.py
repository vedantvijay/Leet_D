# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for lst in lists:
            while lst:
                res.append(lst.val)
                lst = lst.next
        
        res = sorted(res)
        temp = ListNode(0)
        current = temp
        for val in res:
            current.next = ListNode(val)
            current = current.next
        return temp.next