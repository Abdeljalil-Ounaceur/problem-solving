"""
142. Linked List Cycle II
Medium

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer 
is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?

Topics: Hash Table, Linked List, Two Pointers
Companies: Multiple
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Unoptimized Solution - Using Hash Set
        
        Time Complexity: O(n) - Visit each node at most once
        Space Complexity: O(n) - Store nodes in hash set
        
        Algorithm:
        1. Use a dummy node to simplify the logic
        2. Iterate through the linked list
        3. Check if current node is in the seen set
        4. If yes, it's the start of the cycle
        5. If no, add to seen set and continue
        6. If we reach end without finding a cycle, return None
        """
        node = dummy = ListNode(1, head)
        seen = set()
        
        while node.next:
            node = node.next
            if node in seen:
                return node
            else:
                seen.add(node)
        
        return None


class OptimalSolution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Optimal Solution - Floyd's Cycle Detection Algorithm (Two Pointers)
        
        Time Complexity: O(n) - Two passes through the list
        Space Complexity: O(1) - Only use two pointers
        
        Algorithm (Two Phase Approach):
        
        Phase 1: Detect if a cycle exists
        - Use slow pointer (moves 1 step) and fast pointer (moves 2 steps)
        - If they meet, there's a cycle
        - If fast reaches end, no cycle
        
        Phase 2: Find the start of the cycle
        Mathematical proof:
        - Let's say the distance from head to cycle start is 'a'
        - The distance from cycle start to meeting point is 'b'
        - The remaining distance in cycle is 'c' (so cycle length = b + c)
        
        When they meet:
        - Slow pointer traveled: a + b
        - Fast pointer traveled: a + b + c + b = a + 2b + c
        
        Since fast travels twice the distance:
        2(a + b) = a + 2b + c
        2a + 2b = a + 2b + c
        a = c
        
        This means: distance from head to cycle start equals distance from 
        meeting point to cycle start (going around the cycle).
        
        Therefore:
        - Reset slow pointer to head
        - Move both pointers one step at a time
        - They will meet at the cycle start
        """
        slow = fast = head
        
        # Step 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # No cycle found
        
        # Step 2: Find the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow


# Test the solutions
if __name__ == "__main__":
    # Helper function to create a linked list with a cycle
    def create_linked_list_with_cycle(values, pos):
        """Create a linked list with a cycle at position pos"""
        if not values:
            return None
        
        nodes = [ListNode(val) for val in values]
        
        # Connect the nodes
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        
        # Create cycle if pos is valid
        if pos >= 0:
            nodes[-1].next = nodes[pos]
        
        return nodes[0]
    
    # Test cases
    test_cases = [
        ([3, 2, 0, -4], 1),  # Cycle at position 1
        ([1, 2], 0),         # Cycle at position 0
        ([1], -1),           # No cycle
    ]
    
    for values, pos in test_cases:
        head = create_linked_list_with_cycle(values, pos)
        
        # Test unoptimized solution
        sol1 = Solution()
        result1 = sol1.detectCycle(head)
        
        # Reset the list for the second test
        head = create_linked_list_with_cycle(values, pos)
        
        # Test optimal solution
        sol2 = OptimalSolution()
        result2 = sol2.detectCycle(head)
        
        if pos >= 0:
            print(f"Input: {values}, pos={pos}")
            print(f"Unoptimized: Found cycle at node with value {result1.val if result1 else 'None'}")
            print(f"Optimal: Found cycle at node with value {result2.val if result2 else 'None'}")
        else:
            print(f"Input: {values}, pos={pos}")
            print(f"Unoptimized: No cycle found")
            print(f"Optimal: No cycle found")
        print()
