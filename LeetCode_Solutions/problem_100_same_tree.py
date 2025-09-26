"""
LeetCode Problem 100: Same Tree

Problem Statement:
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
- The number of nodes in both trees is in the range [0, 100].
- -10^4 <= Node.val <= 10^4

Time Complexity: O(min(m,n)) where m and n are the number of nodes in trees p and q
Space Complexity: O(min(m,n)) due to recursion stack depth
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Recursive solution to check if two binary trees are identical.
        
        The logic is:
        1. If both nodes exist, check if their values are equal AND recursively check left and right subtrees
        2. If either node is None, they must both be None to be considered the same
        
        Args:
            p: Root of first binary tree
            q: Root of second binary tree
            
        Returns:
            bool: True if trees are identical, False otherwise
        """
        if p and q:
            # Both nodes exist - check value equality and recursively check subtrees
            return (p.val == q.val and 
                   self.isSameTree(p.left, q.left) and 
                   self.isSameTree(p.right, q.right))
        else:
            # At least one node is None - they're same only if both are None
            return p == q

# Alternative iterative solution using stack
class SolutionIterative:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Iterative solution using stack to avoid recursion.
        
        Time Complexity: O(min(m,n))
        Space Complexity: O(min(m,n)) for the stack
        """
        stack = [(p, q)]
        
        while stack:
            node1, node2 = stack.pop()
            
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
                
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
            
        return True

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [1,2,3] vs [1,2,3] - should return True
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(f"Test 1: {solution.isSameTree(p1, q1)}")  # Expected: True
    
    # Test case 2: [1,2] vs [1,null,2] - should return False  
    p2 = TreeNode(1, TreeNode(2), None)
    q2 = TreeNode(1, None, TreeNode(2))
    print(f"Test 2: {solution.isSameTree(p2, q2)}")  # Expected: False
    
    # Test case 3: [1,2,1] vs [1,1,2] - should return False
    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))
    print(f"Test 3: {solution.isSameTree(p3, q3)}")  # Expected: False
