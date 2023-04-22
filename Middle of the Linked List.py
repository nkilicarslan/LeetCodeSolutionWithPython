from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    # this function will return the middle node of the linked list
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create two variables to store the current node
        curr_ptr = tmp_ptr = head
        # iterate over the linked list until the tmp_ptr or the next_ptr of the tmp reaches the end of the linked list
        while tmp_ptr and tmp_ptr.next:
            # update the tmp_ptr twice and the curr_ptr once
            tmp_ptr = tmp_ptr.next
            tmp_ptr = tmp_ptr.next
            curr_ptr = curr_ptr.next
        # return the curr_ptr
        return curr_ptr
