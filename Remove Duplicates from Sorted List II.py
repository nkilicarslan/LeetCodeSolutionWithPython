from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a ListNode
        prev = ListNode()
        prev.next = head
        tmp_head = prev
        if not head:
            return head
        is_duplicate_or_not = False
        while head.next:
            if head.val == head.next.val:
                is_duplicate_or_not = True
                head = head.next
            elif is_duplicate_or_not == True:
                prev.next = head.next
                head = head.next
                is_duplicate_or_not = False
            else:
                head = head.next
                prev = prev.next
        if is_duplicate_or_not == True:
            prev.next = None
        return tmp_head.next
# create a test case for the deleteDuplicates function the input is [1,1,1,2,3] and the output is [2,3]
a  = ListNode(1)
b = ListNode(1)
c = ListNode(1)
d = ListNode(2)
e = ListNode(3)
a.next = b
b.next = c
c.next = d
d.next = e
# create an instance of the Solution class
solution = Solution()
# call the deleteDuplicates function with the head of the test case
solution.deleteDuplicates(a)

