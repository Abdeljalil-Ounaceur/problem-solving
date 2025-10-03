"""
LeetCode Problem 236: Lowest Common Ancestor of a Binary Tree

Difficulty: Medium
Topics: Tree, Depth-First Search, Binary Tree

Problem Description:
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes 
p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a 
descendant of itself)."

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the tree.

Solution Approach:
This is a general binary tree (not BST), so we can't use value comparisons.
We use recursive DFS to search for both nodes.

Key Insight:
- If a node finds one of the target nodes, it returns that node
- If a node receives non-null returns from both left and right subtrees, it's the LCA
- Otherwise, return whichever subtree returned non-null (propagating the finding upward)

Time Complexity: O(n) where n is the number of nodes
- In worst case, we visit all nodes

Space Complexity: O(h) where h is the height of the tree
- Recursion stack depth equals tree height
- Worst case (skewed tree): O(n)
- Best case (balanced tree): O(log n)

Acceptance Rate: ~50%
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Optimal recursive DFS solution.
        
        The algorithm:
        1. Base case: if root is None or root is p or q, return root
        2. Recursively search in left and right subtrees
        3. If both left and right return non-null, current root is LCA
        4. Otherwise, return the non-null result (or None if both null)
        
        Why this works:
        - If we find p or q, we return it immediately
        - The LCA is the first node that has p in one subtree and q in another
        - If one node is ancestor of another, the ancestor is returned first
        """
        # Base case: empty node or found one of the target nodes
        if not root:
            return None
        
        if root in (p, q):
            return root
        
        # Recursively search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both subtrees return non-null, current node is the LCA
        if left and right:
            return root
        else:
            # Return whichever is non-null (or None if both are null)
            # This propagates the finding upward in the recursion
            return left or right


# Alternative solution with clearer logic flow
class Solution_Alternative:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Same approach with more explicit logic.
        """
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # Case 1: Found both nodes in different subtrees
        if left and right:
            return root
        
        # Case 2: Both nodes in left subtree
        if left:
            return left
        
        # Case 3: Both nodes in right subtree
        if right:
            return right
        
        # Case 4: Found nothing (shouldn't happen per problem constraints)
        return None
