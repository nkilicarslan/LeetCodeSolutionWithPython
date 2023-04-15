# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # this function will return true if the linked list is a palindrome
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # create a list to store the values of the linked list
        store_values = []
        # iterate over the linked list and store the values in the list
        while head:
            store_values.append(head.val)
            head = head.next
        # check if the list is a palindrome and return the result
        return store_values[::-1] == store_values
