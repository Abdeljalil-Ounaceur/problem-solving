"""
LeetCode Problem 102: Binary Tree Level Order Traversal
Difficulty: Medium
Topics: Tree, Breadth-First Search, Binary Tree

Problem Description:
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Examples:
- Input: root = [3,9,20,null,null,15,7] → Output: [[3],[9,20],[15,7]]
- Input: root = [1] → Output: [[1]]
- Input: root = [] → Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 2000]
- -1000 <= Node.val <= 1000
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
    Initial DFS Solution:
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (recursion stack)
    
    Note: This approach uses instance variable which can cause issues with multiple calls
    """
    def __init__(self):
        self.list = []
    
    def levelOrder_initial(self, root: Optional[TreeNode], depth=0) -> List[List[int]]:
        if root:
            if len(self.list) > depth:
                self.list[depth].append(root.val)
            else:
                self.list.append([root.val])

            self.levelOrder_initial(root.left, depth+1)    
            self.levelOrder_initial(root.right, depth+1)
        
        return self.list

class SolutionCleanDFS:
    """
    Cleaner DFS Solution:
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (recursion stack)
    
    This approach avoids instance variables and uses a nested helper function
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def dfs(node, depth):
            if not node:
                return
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return res

class SolutionOptimalBFS:
    """
    Optimal BFS Solution:
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(w) where w is the maximum width of the tree
    
    This is the most intuitive approach for level order traversal using a queue
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res, q = [], deque([root])
        
        while q:
            level = []
            # Process all nodes at current level
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                # Add children to queue for next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        
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
    
    # Test all solutions
    sol_dfs = SolutionCleanDFS()
    sol_bfs = SolutionOptimalBFS()
    
    print("DFS Solution:", sol_dfs.levelOrder(root))
    print("BFS Solution:", sol_bfs.levelOrder(root))
    
    # Expected output: [[3], [9, 20], [15, 7]]

if __name__ == "__main__":
    test_solutions()
