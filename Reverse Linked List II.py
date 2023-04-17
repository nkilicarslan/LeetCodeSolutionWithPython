# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        tmp_head = head
        left_ptr = -1
        right_ptr = -1
        reversed_nodes = []
        pointer = 1
        while tmp_head and pointer != left:
            pointer += 1
            left_ptr = tmp_head
            tmp_head = tmp_head.next

        while tmp_head and pointer != right:
            reversed_nodes.append(tmp_head)
            right_ptr = tmp_head
            tmp_head = tmp_head.next
            pointer += 1
        # take the reverse of the reversed_nodes with python slicing
        reversed_nodes = reversed_nodes[::-1]
        if len(reversed_nodes) != 0:
            left_ptr.next = reversed_nodes[0]
        for i in range(len(reversed_nodes) - 1):
            reversed_nodes[i].next = reversed_nodes[i+1]
        if len(reversed_nodes) != 0:
            reversed_nodes[-1].next = right_ptr.next
        return head

