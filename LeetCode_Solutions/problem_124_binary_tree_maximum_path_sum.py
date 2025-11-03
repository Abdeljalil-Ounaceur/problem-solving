"""
LeetCode Problem 124: Binary Tree Maximum Path Sum
Difficulty: Hard
Topics: Tree, Depth-First Search, Dynamic Programming, Binary Tree

Problem Description:
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:
- The number of nodes in the tree is in the range [1, 3 * 10^4].
- -1000 <= Node.val <= 1000
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        
        def max_path_sum(node):
            nonlocal max_sum
            if not node:
                return 0
            max_left = max(max_path_sum(node.left), 0)
            max_right = max(max_path_sum(node.right), 0)
            
            current_path = node.val + max_left + max_right
            max_sum = max(max_sum, current_path)
            
            return node.val + max(max_left, max_right)
        
        max_path_sum(root)
        return max_sum

# Helper function to create a tree from a list (for testing)
def create_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        current = queue.pop(0)
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    root1 = create_tree([1,2,3])
    print(f"Test 1: {solution.maxPathSum(root1)}") # Expected: 6

    # Test case 2
    root2 = create_tree([-10,9,20,None,None,15,7])
    print(f"Test 2: {solution.maxPathSum(root2)}") # Expected: 42
