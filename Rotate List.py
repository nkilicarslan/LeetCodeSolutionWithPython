# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next == None:
            return head
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        def rotate_and_return(head):
            tmp_head = head
            last_node = None
            while head.next:
                if head.next.next == None:
                    last_node = head.next
                    head.next = None
                    break
                head = head.next
            last_node.next = tmp_head
            return last_node
        length = get_length(head)
        k = k % length
        for i in range(k):
            head = rotate_and_return(head)
        return head

