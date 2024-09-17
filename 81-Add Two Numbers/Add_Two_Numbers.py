# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    pass


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def calculate(remainder, node1, node2):
            if not node1 and not node2 and remainder == 0:
                return None

            node_val1 = node1.val if node1 else 0
            node_val2 = node2.val if node2 else 0

            result = node_val1 + node_val2 + remainder
            currentnode = ListNode(result % 10)
            remainder = result // 10

            next1 = node1.next if node1 else None
            next2 = node2.next if node2 else None

            currentnode.next = calculate(remainder, next1, next2)
            return currentnode

        return calculate(0, l1, l2)
