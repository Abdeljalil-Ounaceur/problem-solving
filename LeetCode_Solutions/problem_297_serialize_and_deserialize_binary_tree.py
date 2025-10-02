"""
LeetCode Problem 297: Serialize and Deserialize Binary Tree
Difficulty: Hard
Topics: String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree

Problem:
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
    Initial Solution: Using empty strings for null nodes
    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def addTree(node):
            if node:
                return f"{node.val},{addTree(node.left)},{addTree(node.right)}"
            else:
                return ""

        return addTree(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
            
        q = deque(data.split(","))
        head = TreeNode(int(q.popleft()))

        def composeTree(head, q):
            lvalue = q.popleft()
            if lvalue:
                head.left = TreeNode(int(lvalue))
                composeTree(head.left, q)

            rvalue = q.popleft()
            if rvalue:
                head.right = TreeNode(int(rvalue))
                composeTree(head.right, q)
        
        composeTree(head, q)

        return head


# Optimal Solution: Using "null" strings for null nodes
class CodecOptimal:
    """
    Optimal Solution: Using explicit "null" markers for cleaner parsing
    
    Approach:
    - Use preorder traversal for serialization with "null" markers for empty nodes
    - Use iterator pattern for deserialization to avoid index management
    - Recursive deserialization that naturally handles the preorder structure
    
    Time Complexity: O(n) for both serialize and deserialize
    Space Complexity: O(n) for the serialized string and O(h) for recursion stack
    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def addTree(node):
            if node:
                return f"{node.val},{addTree(node.left)},{addTree(node.right)}"
            else:
                return "null"

        return addTree(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
            
        tokens = iter(data.split(","))

        def composeTree():
            val = next(tokens)

            if val == "null":
                return None
            
            node = TreeNode(int(val))
            node.left = composeTree()
            node.right = composeTree()

            return node
        
        return composeTree()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
