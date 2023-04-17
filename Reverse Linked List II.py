# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    # this function will reverse the linked list between the left and right pointers
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # create a dummy node
        dummy = ListNode(0, head)
        # create a tmp_head to store the head
        tmp_head = head
        # create a left_ptr and right_ptr to store the left and right pointers
        left_ptr = dummy
        left_ptr.next = head
        right_ptr = -1
        # create a reversed_nodes list to store the reversed nodes
        reversed_nodes = []
        pointer = 1
        # iterate over the linked list to the left pointer
        while tmp_head and pointer != left:
            pointer += 1
            left_ptr = tmp_head
            tmp_head = tmp_head.next
        # iterate over the linked list to the right pointer and append the nodes to the reversed_nodes list
        while tmp_head and pointer != right + 1 and left != right:
            reversed_nodes.append(tmp_head)
            tmp_head = tmp_head.next
            pointer += 1
        # take the reverse of the reversed_nodes with python slicing
        reversed_nodes = reversed_nodes[::-1]
        # if the reversed_nodes list is not empty update the left_ptr.next
        if len(reversed_nodes) != 0:
            left_ptr.next = reversed_nodes[0]
        # iterate over the reversed_nodes list and update the next pointers
        for i in range(len(reversed_nodes) - 1):
            reversed_nodes[i].next = reversed_nodes[i+1]
        # if the reversed_nodes list is not empty update the last node's next pointer
        if len(reversed_nodes) != 0:
            reversed_nodes[-1].next = tmp_head
        # return the dummy.next
        return dummy.next
