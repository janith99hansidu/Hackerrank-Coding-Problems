# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # go to the end case
        if not head or not head.next:
            return head

        # go to the next node
        reversed_list = self.reverseList(head.next)

        # what happens in each head
        head.next.next = head
        head.next = None

        return reversed_list
