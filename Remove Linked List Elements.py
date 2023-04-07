# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # create a dummy node
        dummy = ListNode(0)
        # point the dummy node to the head
        dummy.next = head
        # create a curr pointer
        curr = dummy
        # while the curr.next is not None
        while curr.next:
            # if the curr.next.value is equal to the val then move the pointer to the next node
            if curr.next.value == val:
                curr.next = curr.next.next
            # otherwise move the curr pointer to the next node
            else:
                curr = curr.next
        # return the head of the linked list
        return dummy.next
