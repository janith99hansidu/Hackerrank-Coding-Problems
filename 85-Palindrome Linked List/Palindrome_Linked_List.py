# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.frontPointer = head

        def recursively_check(current):

            # if the current is None return true
            # sub-problem is traverse to each node
            # connection between sub-problems return true if first and last match
            # if it did not match return false and no other checking

            if current is not None:

                # recursive way to the end of the linked list
                if not recursively_check(current.next):
                    return False

                # Compare the current node's value with the front pointer's value
                if current.val != self.front_pointer.val:
                    return False

                # Move the front pointer forward
                self.front_pointer = self.front_pointer.next

            return True

        return recursively_check(head)

