"""
LeetCode Problem 235: Lowest Common Ancestor of a Binary Search Tree

Difficulty: Medium
Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree

Problem Description:
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes 
p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a 
descendant of itself)."

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the BST.

Solution Approach:
This solution leverages the BST property where left subtree values < root < right subtree values.

Key Insight:
- If both p and q are smaller than root, LCA must be in left subtree
- If both p and q are greater than root, LCA must be in right subtree
- Otherwise, current root is the LCA (one node is on left, one on right, or root is one of them)

Time Complexity: O(h) where h is the height of the tree
- In worst case (skewed tree): O(n)
- In balanced tree: O(log n)

Space Complexity: O(1) - iterative solution uses constant space

Acceptance Rate: 69.2%
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
        Optimal iterative solution using BST properties.
        
        The algorithm:
        1. If both nodes are smaller than root, go left
        2. If both nodes are greater than root, go right
        3. Otherwise, we found the split point (LCA)
        
        Why this works:
        - BST property ensures all left descendants < root < all right descendants
        - LCA is the first node where p and q diverge to different subtrees
        - Or it's one of p/q itself if the other is in its subtree
        """
        while root:
            # Both nodes are in left subtree
            if root.val < min(p.val, q.val):
                root = root.right
            # Both nodes are in right subtree
            elif root.val > max(p.val, q.val):
                root = root.left
            else:
                # Found the split point where p and q diverge
                # This covers three cases:
                # 1. p < root < q
                # 2. q < root < p
                # 3. root == p or root == q
                return root


# Alternative recursive solution (less optimal due to O(h) space for recursion stack)
class Solution_Recursive:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Recursive solution - cleaner but uses O(h) space for call stack.
        
        Time Complexity: O(h)
        Space Complexity: O(h) for recursion stack
        """
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
