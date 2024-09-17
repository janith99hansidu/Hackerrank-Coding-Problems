# Define the ListNode class
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    # Base case: if head is None or there's only one node left
    if head is None or head.next is None:
        return head

    # Initialize two pointers
    first_node = head
    second_node = head.next

    # Swap the nodes
    first_node.next = swapPairs(second_node.next)
    second_node.next = first_node

    # Now the second node is the new head of the swapped pair
    return second_node


# Test the function
if __name__ == '__main__':
    # Create a linked list: 1 -> 2 -> 3 -> 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    # After calling swapPairs, the list should look like: 2 -> 1 -> 4 -> 3
    new_head = swapPairs(head)

    # Print the swapped list
    current = new_head
    while current:
        print(current.val)
        current = current.next
