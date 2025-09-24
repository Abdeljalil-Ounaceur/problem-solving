"""
LeetCode Problem 21: Merge Two Sorted Lists

Problem Statement:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Examples:
1. Input: list1 = [1,2,4], list2 = [1,3,4]
   Output: [1,1,2,3,4,4]

2. Input: list1 = [], list2 = []
   Output: []

3. Input: list1 = [], list2 = [0]
   Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Optimal Solution: Dummy Node Approach
        
        Time Complexity: O(n + m) where n and m are lengths of list1 and list2
        Space Complexity: O(1) - only using constant extra space
        
        Approach:
        1. Create a dummy node to simplify edge cases
        2. Use a tail pointer to build the merged list
        3. Compare values and attach the smaller node
        4. Move the pointer of the selected list
        5. Attach any remaining nodes
        
        This approach is cleaner and more readable than the alternative solution.
        """
        dummy = ListNode(-1)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach remaining nodes (at most one of these will be non-null)
        tail.next = list1 if list1 else list2
        
        return dummy.next

    def mergeTwoListsAlternative(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Alternative Solution: Direct Pointer Manipulation
        
        Time Complexity: O(n + m)
        Space Complexity: O(1)
        
        This approach directly manipulates pointers without using a dummy node.
        While it works, it's more complex and harder to understand than the optimal solution.
        """
        if (list1 and list2):
            head = list1 if list1.val <= list2.val else list2
        elif(list1):
            head = list1
        elif(list2):
            head = list2
        else:
            return None

        while(list1 and list2):
            if list1.val <= list2.val:
                while list1.next and list1.next.val <= list2.val:
                    list1 = list1.next
                list1.next, list1 = list2, list1.next
            else:
                while list2.next and list2.next.val <= list1.val:
                    list2 = list2.next
                list2.next, list2 = list1, list2.next

        return head

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

def linked_list_to_array(head):
    """Helper function to convert linked list to array for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [1,2,4] and [1,3,4] -> [1,1,2,3,4,4]
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Test 1: {linked_list_to_array(merged)}")  # Expected: [1,1,2,3,4,4]
    
    # Test case 2: [] and [] -> []
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Test 2: {linked_list_to_array(merged)}")  # Expected: []
    
    # Test case 3: [] and [0] -> [0]
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Test 3: {linked_list_to_array(merged)}")  # Expected: [0]
    
    # Test case 4: [5] and [1,2,4] -> [1,2,4,5]
    list1 = create_linked_list([5])
    list2 = create_linked_list([1, 2, 4])
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Test 4: {linked_list_to_array(merged)}")  # Expected: [1,2,4,5]
