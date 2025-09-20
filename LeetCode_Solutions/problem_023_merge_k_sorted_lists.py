"""
LeetCode Problem 23: Merge k Sorted Lists
Difficulty: Hard
Topics: Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort

Problem Description:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.
"""

from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        """
        Merge k sorted linked lists using a min heap (priority queue).
        
        Time Complexity: O(N log k) where N is the total number of nodes and k is the number of lists
        Space Complexity: O(k) for the heap
        
        Approach:
        1. Initialize a min heap with the first node of each non-empty list
        2. Use the index as a tiebreaker to handle nodes with equal values
        3. Pop the smallest node from heap, add it to result, and push its next node
        4. Continue until heap is empty
        """
        h = []
        
        # Initialize heap with first node of each non-empty list
        for index in range(len(lists)):
            node = lists[index]
            if node:
                heappush(h, (node.val, index, node))

        # Handle empty input
        if not h:
            return None
        
        # Create dummy head for result list
        dummy = ListNode(0)
        tail = dummy

        # Process nodes from heap
        while h:
            val, index, node = heappop(h)
            tail.next = node
            tail = tail.next
            
            # Add next node from same list to heap if it exists
            if node.next:
                heappush(h, (node.next.val, index, node.next))
        
        return dummy.next

# Alternative solution using divide and conquer approach
class SolutionDivideConquer:
    def mergeKLists(self, lists):
        """
        Merge k sorted linked lists using divide and conquer.
        
        Time Complexity: O(N log k) where N is the total number of nodes and k is the number of lists
        Space Complexity: O(log k) for recursion stack
        """
        if not lists:
            return None
        
        while len(lists) > 1:
            merged_lists = []
            
            # Merge pairs of lists
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(self.mergeTwoLists(l1, l2))
            
            lists = merged_lists
        
        return lists[0]
    
    def mergeTwoLists(self, l1, l2):
        """Helper function to merge two sorted linked lists."""
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # Append remaining nodes
        tail.next = l1 or l2
        
        return dummy.next

# Test cases
def test_solution():
    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def linked_list_to_array(head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    solution = Solution()
    
    # Test case 1
    lists1 = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    result1 = solution.mergeKLists(lists1)
    print(f"Test 1: {linked_list_to_array(result1)}")  # Expected: [1, 1, 2, 3, 4, 4, 5, 6]
    
    # Test case 2
    lists2 = []
    result2 = solution.mergeKLists(lists2)
    print(f"Test 2: {linked_list_to_array(result2)}")  # Expected: []
    
    # Test case 3
    lists3 = [create_linked_list([])]
    result3 = solution.mergeKLists(lists3)
    print(f"Test 3: {linked_list_to_array(result3)}")  # Expected: []

if __name__ == "__main__":
    test_solution()
