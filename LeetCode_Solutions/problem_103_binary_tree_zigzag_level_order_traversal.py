"""
LeetCode Problem 103: Binary Tree Zigzag Level Order Traversal
Difficulty: Medium
Topics: Tree, Breadth-First Search, Binary Tree

Problem Description:
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Examples:
- Input: root = [3,9,20,null,null,15,7] → Output: [[3],[20,9],[15,7]]
- Input: root = [1] → Output: [[1]]
- Input: root = [] → Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 2000]
- -100 <= Node.val <= 100
"""

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Initial Solution using reverse():
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(w) where w is the maximum width of the tree
    
    This approach builds each level normally then reverses odd-indexed levels
    """
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res, q = [], deque([root])
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Reverse every other level (odd-indexed levels)
            if len(res) % 2 == 1:
                level.reverse()

            res.append(level)
        
        return res

class SolutionOptimal:
    """
    Optimal Solution using deque with directional appending:
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(w) where w is the maximum width of the tree
    
    This approach avoids the reverse() operation by using deque's appendleft()
    More efficient as it builds the level in the correct order from the start
    """
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res, q = [], deque([root])
        left_to_right = True   # flag to track direction
        
        while q:
            level = deque()
            for _ in range(len(q)):
                node = q.popleft()
                
                # Add to appropriate end based on direction
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(list(level))   # convert deque to list
            left_to_right = not left_to_right   # flip direction
        
        return res

# Test cases
def test_solutions():
    # Create test tree: [3,9,20,null,null,15,7]
    #       3
    #      / \
    #     9   20
    #        /  \
    #       15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    # Test both solutions
    sol_initial = Solution()
    sol_optimal = SolutionOptimal()
    
    print("Initial Solution:", sol_initial.zigzagLevelOrder(root))
    print("Optimal Solution:", sol_optimal.zigzagLevelOrder(root))
    
    # Expected output: [[3], [20, 9], [15, 7]]
    
    # Test edge cases
    print("Empty tree:", sol_optimal.zigzagLevelOrder(None))
    
    single_node = TreeNode(1)
    print("Single node:", sol_optimal.zigzagLevelOrder(single_node))

if __name__ == "__main__":
    test_solutions()
