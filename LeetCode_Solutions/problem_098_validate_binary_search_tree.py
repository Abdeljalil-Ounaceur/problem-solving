"""
LeetCode Problem 98: Validate Binary Search Tree
Difficulty: Medium
Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree

Problem:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys strictly less than the node's key.
- The right subtree of a node contains only nodes with keys strictly greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val=float("-inf"), max_val=float("inf")) -> bool:
        """
        Validate if a binary tree is a valid BST using DFS with range validation.
        
        Approach:
        - Use recursive DFS to traverse the tree
        - Pass down valid range (min_val, max_val) for each node
        - Each node's value must be strictly within its valid range
        - Left subtree gets range (min_val, root.val)
        - Right subtree gets range (root.val, max_val)
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree (recursion stack)
        
        Args:
            root: Root node of the binary tree
            min_val: Minimum valid value for current node (exclusive)
            max_val: Maximum valid value for current node (exclusive)
            
        Returns:
            bool: True if tree is a valid BST, False otherwise
        """
        return not root or (
                root.val > min_val and root.val < max_val and (
                    (
                        not root.left or self.isValidBST(root.left, min_val, root.val)
                    ) and (
                        not root.right or self.isValidBST(root.right, root.val, max_val)
                    )
                )
            )


# Alternative Solution: Iterative Inorder Traversal
class SolutionIterative:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Validate BST using iterative inorder traversal.
        
        Approach:
        - Inorder traversal of a BST should produce values in strictly increasing order
        - Use a stack to simulate the recursion
        - Track the previous value and ensure each new value is greater
        
        Time Complexity: O(n)
        Space Complexity: O(h) for the stack
        """
        stack = []
        prev = float("-inf")
        current = root
        
        while stack or current:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process current node
            current = stack.pop()
            
            # Check if values are in strictly increasing order
            if current.val <= prev:
                return False
            prev = current.val
            
            # Move to right subtree
            current = current.right
        
        return True
