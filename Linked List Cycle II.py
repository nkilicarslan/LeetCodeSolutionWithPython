# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # this function will return the node where the cycle begins
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a variable to store the values of the nodes
        keep_ptr_val = []
        # iterate over the linked list
        while head:
            # if the value of the node is not in the keep_ptr_val, append it to the keep_ptr_val
            if head not in keep_ptr_val:
                keep_ptr_val.append(head)
                # move the pointer to the next node
                head = head.next
            # otherwise return the node
            else:
                return head
        # if there is no cycle, return None
        return None
