"""
LeetCode Problem #25: Reverse Nodes in k-Group
Difficulty: Hard
Topics: Linked List, Recursion

Problem Description:
Given the head of a linked list, reverse the nodes of the list k at a time, 
and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, 
should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]

Example 2:
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]

Constraints:
    - The number of nodes in the list is n.
    - 1 <= k <= n <= 5000
    - 0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        Reverse nodes in k-group using O(1) extra space.
        
        Approach:
        1. Use dummy node to simplify head edge case handling
        2. Iterate through the list in groups of k nodes
        3. For each complete group of k nodes:
           - Reverse the k nodes in-place
           - Connect the reversed group to the previous part
           - Move to the next group
        4. If the last group has fewer than k nodes, leave them as is
        
        Time Complexity: O(n) - each node is visited exactly twice (once to count, once to reverse)
        Space Complexity: O(1) - only using pointers, no extra space
        
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        last = dummy = ListNode(-1, head)
        node = head
        
        while node:
            first = node
            i = 0
            # Count k nodes
            while i < k and node:
                node = node.next
                i += 1
            
            # If we don't have k nodes, stop
            if i < k:
                break
            
            # Reverse k nodes
            prev, curr = None, first
            while curr != node:
                curr.next, prev, curr = prev, curr, curr.next
            
            # Connect reversed group: last->prev, first->node, update last
            last.next, first.next, last = prev, node, first
            
        return dummy.next


"""
Alternative Solution: Recursive Approach

class Solution(object):
    def reverseKGroup(self, head, k):
        # Count if we have k nodes
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        
        # If we have k nodes, reverse them
        if count == k:
            # Reverse k nodes
            prev = None
            curr = head
            for _ in range(k):
                curr.next, prev, curr = prev, curr, curr.next
            
            # Recursively reverse the rest and connect
            head.next = self.reverseKGroup(curr, k)
            return prev
        
        return head

Time Complexity: O(n)
Space Complexity: O(n/k) - recursion stack depth
"""
