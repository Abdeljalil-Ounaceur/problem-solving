"""
LeetCode Problem #206: Reverse Linked List
Difficulty: Easy
Topics: Linked List, Recursion
Companies: Amazon, Microsoft, Apple, Google, Facebook

Problem Description:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

Acceptance Rate: 79.6%
Accepted: 5,597,070/7M
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative approach to reverse a linked list.
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) - only using constant extra space
        
        Algorithm:
        1. Use two pointers: left (previous) and right (current)
        2. Iterate through the list, reversing the direction of each link
        3. Keep track of the next node before breaking the link
        """
        left, right = None, head
        while right:
            nxt = right.next  # Store next node before breaking the link
            right.next = left  # Reverse the link
            left = right      # Move left pointer forward
            right = nxt       # Move right pointer forward
        return left  # left is now the new head of the reversed list
    
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive approach to reverse a linked list.
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(n) due to recursion stack
        """
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        
        # Recursively reverse the rest of the list
        new_head = self.reverseListRecursive(head.next)
        
        # Reverse the current connection
        head.next.next = head
        head.next = None
        
        return new_head


# Test cases
def test_reverse_linked_list():
    """Test function to verify the solution works correctly."""
    
    def create_linked_list(values):
        """Helper function to create a linked list from a list of values."""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def linked_list_to_list(head):
        """Helper function to convert linked list back to Python list."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    solution = Solution()
    
    # Test case 1: [1,2,3,4,5] -> [5,4,3,2,1]
    head1 = create_linked_list([1, 2, 3, 4, 5])
    reversed1 = solution.reverseList(head1)
    assert linked_list_to_list(reversed1) == [5, 4, 3, 2, 1]
    
    # Test case 2: [1,2] -> [2,1]
    head2 = create_linked_list([1, 2])
    reversed2 = solution.reverseList(head2)
    assert linked_list_to_list(reversed2) == [2, 1]
    
    # Test case 3: [] -> []
    head3 = create_linked_list([])
    reversed3 = solution.reverseList(head3)
    assert linked_list_to_list(reversed3) == []
    
    # Test recursive solution
    head4 = create_linked_list([1, 2, 3, 4, 5])
    reversed4 = solution.reverseListRecursive(head4)
    assert linked_list_to_list(reversed4) == [5, 4, 3, 2, 1]
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_reverse_linked_list()
