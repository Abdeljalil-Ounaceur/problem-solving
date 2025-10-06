"""
LeetCode Problem 133: Clone Graph
Difficulty: Medium
Topics: Hash Table, Depth-First Search, Breadth-First Search, Graph

Problem Description:
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Constraints:
- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

Time Complexity: O(N + M) where N is the number of nodes and M is the number of edges
Space Complexity: O(N) for the hash map and queue
"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import defaultdict
from collections import deque


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clone a graph using BFS approach with hash map to track cloned nodes.
        
        Algorithm:
        1. Handle edge case: if input node is None, return None
        2. Create a hash map to store mapping from original nodes to cloned nodes
        3. Create the first cloned node and add original node to queue
        4. Use BFS to traverse all nodes:
           - For each neighbor of current node:
             - If neighbor not cloned yet, create clone and add to queue
             - Add cloned neighbor to current cloned node's neighbors list
        5. Return the cloned version of the input node
        
        Args:
            node: Reference to a node in the original graph
            
        Returns:
            Reference to the corresponding node in the cloned graph
        """
        if not node:
            return None

        # Hash map to store mapping from original nodes to cloned nodes
        mapper = {node: Node(node.val)}
        remaining = deque([node])

        while remaining:
            current = remaining.popleft()
            for neighbor in current.neighbors:
                if neighbor not in mapper:
                    # Create clone of neighbor if not already cloned
                    mapper[neighbor] = Node(neighbor.val)
                    remaining.append(neighbor)
                # Add cloned neighbor to current cloned node's neighbors
                mapper[current].neighbors.append(mapper[neighbor])
        
        return mapper[node]


# Alternative DFS Solution:
class SolutionDFS:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clone a graph using DFS approach with hash map.
        
        Time Complexity: O(N + M)
        Space Complexity: O(N) for hash map + O(N) for recursion stack = O(N)
        """
        if not node:
            return None
        
        # Hash map to store cloned nodes
        cloned = {}
        
        def dfs(node):
            if node in cloned:
                return cloned[node]
            
            # Create clone of current node
            clone = Node(node.val)
            cloned[node] = clone
            
            # Recursively clone all neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)


# Test cases
def test_clone_graph():
    """Test the clone graph implementation"""
    
    # Helper function to create graph from adjacency list
    def create_graph(adj_list):
        if not adj_list:
            return None
        
        nodes = {}
        for i in range(len(adj_list)):
            nodes[i + 1] = Node(i + 1)
        
        for i, neighbors in enumerate(adj_list):
            for neighbor_val in neighbors:
                nodes[i + 1].neighbors.append(nodes[neighbor_val])
        
        return nodes[1] if nodes else None
    
    # Helper function to convert graph back to adjacency list for comparison
    def graph_to_adj_list(node):
        if not node:
            return []
        
        visited = set()
        adj_list = {}
        
        def dfs(node):
            if node.val in visited:
                return
            visited.add(node.val)
            adj_list[node.val] = [neighbor.val for neighbor in node.neighbors]
            for neighbor in node.neighbors:
                dfs(neighbor)
        
        dfs(node)
        
        # Convert to list format (1-indexed)
        result = []
        for i in range(1, len(adj_list) + 1):
            result.append(sorted(adj_list.get(i, [])))
        
        return result
    
    solution = Solution()
    
    # Test case 1: [[2,4],[1,3],[2,4],[1,3]]
    adj_list1 = [[2,4],[1,3],[2,4],[1,3]]
    graph1 = create_graph(adj_list1)
    cloned1 = solution.cloneGraph(graph1)
    result1 = graph_to_adj_list(cloned1)
    print(f"Test 1: {result1}")
    assert result1 == [[2,4],[1,3],[2,4],[1,3]]
    
    # Test case 2: [[]]
    adj_list2 = [[]]
    graph2 = create_graph(adj_list2)
    cloned2 = solution.cloneGraph(graph2)
    result2 = graph_to_adj_list(cloned2)
    print(f"Test 2: {result2}")
    assert result2 == [[]]
    
    # Test case 3: []
    cloned3 = solution.cloneGraph(None)
    result3 = graph_to_adj_list(cloned3)
    print(f"Test 3: {result3}")
    assert result3 == []
    
    print("All tests passed!")


if __name__ == "__main__":
    test_clone_graph()
