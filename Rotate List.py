# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # this function will rotate the linked list to the right by k places
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if the linked list is empty or has only one node return the head
        if not head or head.next == None:
            return head
        # create a function to get the length of the linked list
        def get_length(head):
            # create a length variable
            length = 0
            # iterate through the linked list and increment the length variable
            while head:
                length += 1
                head = head.next
            # return the length
            return length
        # create a function to rotate the linked list and return the new head
        def rotate_and_return(head):
            # create a tmp_head variable to store the head
            tmp_head = head
            # create a last_node variable to store the last node
            last_node = None
            # iterate through the linked list and get the last node
            while head.next:
                # if the next node is the last node
                if head.next.next == None:
                    # store the last node and break the loop
                    last_node = head.next
                    head.next = None
                    break
                head = head.next
            # connect the last node to the tmp_head
            last_node.next = tmp_head
            # return the last node
            return last_node
        # get the length of the linked list
        length = get_length(head)
        # get the number of rotations
        k = k % length
        # if k == 0 return the head
        for i in range(k):
            # rotate the linked list and return the new head
            head = rotate_and_return(head)
        # return the head
        return head

