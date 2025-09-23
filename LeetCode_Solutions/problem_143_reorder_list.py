"""
143. Reorder List
Solved
Medium
Topics
Companies

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
 
Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

 
Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        """Helper function to reverse a linked list"""
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        Algorithm:
        1. Find the middle of the list using slow/fast pointers
        2. Split the list into two halves
        3. Reverse the second half
        4. Merge the two halves alternately
        
        Time Complexity: O(n) - single pass to find middle, O(n) to reverse, O(n) to merge
        Space Complexity: O(1) - only using pointers
        
        Performance: Beats 100.00% of users
        """
        if not head or not head.next:
            return
            
        # Step 1: Find the middle of the list
        slow = fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Split the list into two halves
        second_half = slow.next
        slow.next = None  # Cut the connection

        # Step 3: Reverse the second half
        first = head
        second = self.reverseList(second_half)

        # Step 4: Merge the two halves alternately
        while first and second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2


# Test cases for verification
def create_linked_list(values):
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
    
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    """Helper function to print linked list values"""
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [1,2,3,4] -> [1,4,2,3]
    head1 = create_linked_list([1, 2, 3, 4])
    print("Before reorder:", print_linked_list(head1))
    solution.reorderList(head1)
    print("After reorder:", print_linked_list(head1))
    print("Expected: [1, 4, 2, 3]")
    print()
    
    # Test case 2: [1,2,3,4,5] -> [1,5,2,4,3]
    head2 = create_linked_list([1, 2, 3, 4, 5])
    print("Before reorder:", print_linked_list(head2))
    solution.reorderList(head2)
    print("After reorder:", print_linked_list(head2))
    print("Expected: [1, 5, 2, 4, 3]")
