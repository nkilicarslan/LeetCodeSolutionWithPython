# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # this function will return the linked list without duplicates, delete all duplicates such that each element appears only once
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a variable to store the head of the linked list
        head_tmp = head
        # iterate over the linked list while the head and the next of the head is not None
        while head and head.next:
            # if the value of the head is equal to the value of the next of the head
            if head.val == head.next.val:
                # delete the next value with pointing the next of the head to the next of the next of the head
                head.next = head.next.next
                continue
            # if the value of the head is not equal to the value of the next of the head move to the next node
            head = head.next
        # return the head of the linked list
        return head_tmp
