# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Index (0-based) of the node to delete from the start
        k = length - n

        # 2) Use a dummy to handle deleting the head cleanly
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(k):
            prev = prev.next

        # 3) Delete
        prev.next = prev.next.next
        return dummy.next

        
            