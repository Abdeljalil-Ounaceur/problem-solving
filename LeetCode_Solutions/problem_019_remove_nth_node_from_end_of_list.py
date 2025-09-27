"""
LeetCode Problem 19: Remove Nth Node From End of List
Difficulty: Medium
Topics: Linked List, Two Pointers

Problem Description:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Follow up: Could you do this in one pass?
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        My Initial Solution:
        Uses two pointers (fast and slow) with an additional 'old' pointer to track
        the node before the target node for deletion.
        
        Time Complexity: O(L) where L is the length of the linked list
        Space Complexity: O(1)
        """
        old = None
        fast = slow = head
        
        # Move fast pointer n steps ahead
        while n > 0 and fast:
            fast = fast.next
            n -= 1
        
        # Move both pointers until fast reaches the end
        while fast:
            old = slow
            slow, fast = slow.next, fast.next
        
        # Remove the target node
        if old:
            old.next = slow.next
        
        # Return head if we didn't remove the first node, otherwise return the new head
        return head if slow != head else slow.next

class OptimalSolution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Optimal Solution:
        Uses a dummy node to simplify edge case handling and two pointers technique.
        The dummy node eliminates the need to handle the special case of removing the head.
        
        Time Complexity: O(L) where L is the length of the linked list
        Space Complexity: O(1)
        
        Key insight: Using a dummy node makes the algorithm cleaner by avoiding
        special case handling for removing the first node.
        """
        dummy = ListNode(0, head)
        fast = slow = dummy

        # Move fast ahead by n+1 steps
        # We need n+1 because we want slow to point to the node BEFORE the target
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast hits the end
        while fast:
            fast, slow = fast.next, slow.next

        # Remove target node
        slow.next = slow.next.next

        return dummy.next

# Test cases
def create_linked_list(values):
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Helper function to convert linked list to Python list for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_solutions():
    """Test both solutions with the provided examples"""
    solution = Solution()
    optimal_solution = OptimalSolution()
    
    # Test case 1: [1,2,3,4,5], n = 2 -> [1,2,3,5]
    head1 = create_linked_list([1, 2, 3, 4, 5])
    head1_copy = create_linked_list([1, 2, 3, 4, 5])
    
    result1 = solution.removeNthFromEnd(head1, 2)
    result1_optimal = optimal_solution.removeNthFromEnd(head1_copy, 2)
    
    print("Test 1:")
    print(f"My solution: {linked_list_to_list(result1)}")
    print(f"Optimal solution: {linked_list_to_list(result1_optimal)}")
    print(f"Expected: [1, 2, 3, 5]")
    print()
    
    # Test case 2: [1], n = 1 -> []
    head2 = create_linked_list([1])
    head2_copy = create_linked_list([1])
    
    result2 = solution.removeNthFromEnd(head2, 1)
    result2_optimal = optimal_solution.removeNthFromEnd(head2_copy, 1)
    
    print("Test 2:")
    print(f"My solution: {linked_list_to_list(result2)}")
    print(f"Optimal solution: {linked_list_to_list(result2_optimal)}")
    print(f"Expected: []")
    print()
    
    # Test case 3: [1,2], n = 1 -> [1]
    head3 = create_linked_list([1, 2])
    head3_copy = create_linked_list([1, 2])
    
    result3 = solution.removeNthFromEnd(head3, 1)
    result3_optimal = optimal_solution.removeNthFromEnd(head3_copy, 1)
    
    print("Test 3:")
    print(f"My solution: {linked_list_to_list(result3)}")
    print(f"Optimal solution: {linked_list_to_list(result3_optimal)}")
    print(f"Expected: [1]")

if __name__ == "__main__":
    test_solutions()
