# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a list to store the values of the linked list
        values = []
        while head:
            values.append(head.val)
            head = head.next
        # sort the list
        values.sort()
        # create a new linked list
        new_linked_list = ListNode()
        # create a variable to store the head of the new linked list
        head = new_linked_list
        # iterate over the list
        for i in range(len(values)):
            # create a new node
            new_node = ListNode(values[i])
            # assign the new node to the next of the new linked list
            new_linked_list.next = new_node
            # assign the new node to the new linked list
            new_linked_list = new_linked_list.next
        # return the head of the new linked list
        return head.next