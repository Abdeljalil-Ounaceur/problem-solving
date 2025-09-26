"""
LeetCode Problem #104: Maximum Depth of Binary Tree
Difficulty: Easy
Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

Problem Statement:
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    My Initial Solution:
    This solution tracks the depth explicitly as a parameter.
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (recursion stack)
    """
    def maxDepth_initial(self, root: Optional[TreeNode], depth=0) -> int:
        if not root:
            return depth
        else:
            depth += 1
            return max(self.maxDepth_initial(root.left, depth), 
                      self.maxDepth_initial(root.right, depth))
    
    """
    Optimal Solution:
    This is the classic recursive approach that's more elegant and widely used.
    Instead of tracking depth explicitly, we increment on return.
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (recursion stack)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), 
                          self.maxDepth(root.right))

    """
    Alternative Iterative Solution using BFS:
    This uses level-order traversal to count the number of levels.
    Time Complexity: O(n)
    Space Complexity: O(w) where w is the maximum width of the tree
    """
    def maxDepth_iterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        from collections import deque
        queue = deque([root])
        depth = 0
        
        while queue:
            depth += 1
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth

# Test cases
def test_solution():
    sol = Solution()
    
    # Test case 1: [3,9,20,null,null,15,7]
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    assert sol.maxDepth(root1) == 3
    assert sol.maxDepth_initial(root1) == 3
    assert sol.maxDepth_iterative(root1) == 3
    
    # Test case 2: [1,null,2]
    #   1
    #    \
    #     2
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    
    assert sol.maxDepth(root2) == 2
    assert sol.maxDepth_initial(root2) == 2
    assert sol.maxDepth_iterative(root2) == 2
    
    # Test case 3: Empty tree
    assert sol.maxDepth(None) == 0
    assert sol.maxDepth_initial(None) == 0
    assert sol.maxDepth_iterative(None) == 0
    
    # Test case 4: Single node
    root3 = TreeNode(1)
    assert sol.maxDepth(root3) == 1
    assert sol.maxDepth_initial(root3) == 1
    assert sol.maxDepth_iterative(root3) == 1
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
