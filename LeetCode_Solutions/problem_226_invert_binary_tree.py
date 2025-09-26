"""
LeetCode Problem 226: Invert Binary Tree

Problem Statement:
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree (due to recursion stack)
"""

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Recursive solution to invert a binary tree.
        
        The approach is:
        1. Base case: if root is None, return None
        2. Swap the left and right children
        3. Recursively invert the left and right subtrees
        4. Return the root
        
        Args:
            root: Root of the binary tree to invert
            
        Returns:
            TreeNode: Root of the inverted binary tree
        """
        if not root:
            return None
            
        # Swap left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

# Alternative iterative solution using queue (BFS)
class SolutionIterative:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Iterative solution using BFS to invert binary tree.
        
        Time Complexity: O(n)
        Space Complexity: O(w) where w is the maximum width of the tree
        """
        if not root:
            return None
            
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            # Swap left and right children
            node.left, node.right = node.right, node.left
            
            # Add children to queue for processing
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return root

# Alternative iterative solution using stack (DFS)
class SolutionIterativeStack:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Iterative solution using stack (DFS) to invert binary tree.
        
        Time Complexity: O(n)
        Space Complexity: O(h) where h is the height of the tree
        """
        if not root:
            return None
            
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            # Swap left and right children
            node.left, node.right = node.right, node.left
            
            # Add children to stack for processing
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return root

# Helper function to print tree level by level (for testing)
def print_tree_level_order(root):
    """Print binary tree in level order for visualization."""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
        
    return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
    root1 = TreeNode(4)
    root1.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root1.right = TreeNode(7, TreeNode(6), TreeNode(9))
    
    print("Original tree:", print_tree_level_order(root1))
    inverted1 = solution.invertTree(root1)
    print("Inverted tree:", print_tree_level_order(inverted1))
    print()
    
    # Test case 2: [2,1,3] -> [2,3,1]
    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    print("Original tree:", print_tree_level_order(root2))
    inverted2 = solution.invertTree(root2)
    print("Inverted tree:", print_tree_level_order(inverted2))
    print()
    
    # Test case 3: [] -> []
    root3 = None
    print("Original tree:", print_tree_level_order(root3))
    inverted3 = solution.invertTree(root3)
    print("Inverted tree:", print_tree_level_order(inverted3))
