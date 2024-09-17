# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        # end case at the end of the list and empty list
        if not head:
            return head

        # recursive call to the node
        # the connection of problems is the recursion
        head.next = self.removeElements(head.next, val)

        # return the correct value to the connection
        return head.next if head.val == val else head



