"""
LeetCode Problem 141: Linked List Cycle
Difficulty: Easy
Topics: Hash Table, Linked List, Two Pointers

Problem Description:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Examples:
1. Input: head = [3,2,0,-4], pos = 1
   Output: true
   Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

2. Input: head = [1,2], pos = 0
   Output: true
   Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

3. Input: head = [1], pos = -1
   Output: false
   Explanation: There is no cycle in the linked list.

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        OPTIMAL SOLUTION: Floyd's Cycle Detection Algorithm (Two Pointers)
        
        Approach:
        - Use two pointers: slow (moves 1 step) and fast (moves 2 steps)
        - If there's a cycle, fast pointer will eventually meet slow pointer
        - If there's no cycle, fast pointer will reach the end (None)
        
        Time Complexity: O(n) - In worst case, we visit each node once
        Space Complexity: O(1) - Only using two pointers, constant space
        
        This satisfies the follow-up requirement of using O(1) memory!
        """
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next        # Move slow pointer 1 step
            fast = fast.next.next   # Move fast pointer 2 steps
            
            if slow == fast:        # Cycle detected!
                return True
                
        return False  # No cycle found
    
    def hasCycle_unoptimal(self, head: Optional[ListNode]) -> bool:
        """
        UNOPTIMAL SOLUTION: Hash Set Approach
        
        Approach:
        - Use a hash set to store visited nodes
        - Traverse the linked list and check if current node is already visited
        - If visited, there's a cycle; if we reach the end, no cycle
        
        Time Complexity: O(n) - Visit each node once
        Space Complexity: O(n) - Store up to n nodes in the hash set
        
        This solution is still quite good and intuitive, just uses more memory.
        """
        visited = set()
        
        while head:
            if head in visited:     # Node already seen - cycle detected!
                return True
            visited.add(head)       # Mark current node as visited
            head = head.next        # Move to next node
            
        return False  # Reached end without cycle


# Test cases for verification
def create_cycle_list():
    """Helper function to create test cases"""
    # Test case 1: [3,2,0,-4] with pos=1 (cycle)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates cycle back to node2
    
    return node1

def create_no_cycle_list():
    """Helper function to create test case without cycle"""
    # Test case 3: [1] with pos=-1 (no cycle)
    node1 = ListNode(1)
    return node1

def test_solution():
    """Test both solutions"""
    solution = Solution()
    
    # Test with cycle
    cycle_head = create_cycle_list()
    print("Test with cycle:")
    print(f"Optimal solution: {solution.hasCycle(cycle_head)}")  # Should be True
    
    # Recreate for second test (since traversal modifies pointers)
    cycle_head2 = create_cycle_list()
    print(f"Unoptimal solution: {solution.hasCycle_unoptimal(cycle_head2)}")  # Should be True
    
    # Test without cycle
    no_cycle_head = create_no_cycle_list()
    print("\nTest without cycle:")
    print(f"Optimal solution: {solution.hasCycle(no_cycle_head)}")  # Should be False
    
    no_cycle_head2 = create_no_cycle_list()
    print(f"Unoptimal solution: {solution.hasCycle_unoptimal(no_cycle_head2)}")  # Should be False

if __name__ == "__main__":
    test_solution()
