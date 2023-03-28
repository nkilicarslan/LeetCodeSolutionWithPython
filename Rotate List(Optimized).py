# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if the linked list is empty or has only one node
        if not head or head.next == None:
            return head
        # get length of the linked list
        length = 1
        # create a tail pointer
        tail = head
        # iterate through the linked list get the length and the tail
        while tail.next:
            length += 1
            tail = tail.next
        # get the number of rotations
        k = k % length
        # if k == 0 return the head
        if k == 0:
            return head
        # connect the tail to the head
        tail.next = head
        # find the new tail
        new_tail = head
        for i in range(length-k-1):
            new_tail = new_tail.next
        # find the new head
        new_head = new_tail.next
        # break the connection between the new tail and the new head
        new_tail.next = None
        # return the new head
        return new_head
