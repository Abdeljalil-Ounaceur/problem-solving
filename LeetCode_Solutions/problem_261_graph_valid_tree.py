"""
🧩 Problem (LeetCode 261 — Graph Valid Tree)

You are given n nodes labeled 0 to n−1 and a list of edges, where each edges[i] = [u, v] 
represents an undirected edge between nodes u and v.

Determine if these edges form a valid tree.

✔️ A valid tree must be:
- Connected — all nodes are reachable from any node
- Acyclic — no loops exist

💡 Original (Incorrect) Approach - Directed Tree Interpretation
================================================================

The problem was initially interpreted as a directed tree problem (an arborescence).
Because of that:
- Built the graph with directed edges only (graph[u].append(v))
- Used directed DFS cycle detection (visiting + visited sets)
- Then ran a clever "root detection" check: tried both directions of the edge list 
  to make sure there's exactly one root (a node with no parent).

🧠 In other words:
The check was for a directed tree — one root, no cycles, all nodes reachable.

🧾 Initial Code (Directed Tree Version)
"""

from typing import List

class SolutionDirected:
    """
    This is the INCORRECT interpretation treating it as a directed tree.
    It passes tests by coincidence due to symmetry checking both directions.
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)  # treated as directed

        visited, visiting = set(), set()

        def dfs(node):
            if node in visiting:
                return False  # directed cycle
            if node in visited:
                return True
            visiting.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True

        for i in range(n):
            if not dfs(i):
                return False

        # "Single root" test, tried in both directions
        for i in range(2):
            seen = set()
            ok = True
            for u, v in edges:
                if [u, v][i] in seen:
                    ok = False
                    break
                seen.add([u, v][i])
            if ok and len(seen) == n - 1:
                return True
        return False


"""
✅ Why it passed tests:
By pure symmetry — the problem's edge list is undirected,
and the double-check in both directions compensated for the missing reverse edges.
So it coincidentally worked for all official test cases, even though it was based 
on a directed-tree assumption.
"""


"""
🧠 The Optimal (Correct) Solution
==================================

The correct solution just checks if the graph is connected and acyclic — 
nothing about roots or directions.

Key Insights:
1. A tree with n nodes must have exactly n-1 edges
2. Build undirected graph (add edges in both directions)
3. Use DFS with parent tracking to detect cycles
4. Ensure all nodes are visited (connected)

Time Complexity: O(n + e) where n is number of nodes and e is number of edges
Space Complexity: O(n + e) for the graph and recursion stack
"""

class Solution:
    """
    ✅ Optimal Solution (DFS Version)
    
    This is the CORRECT approach for undirected tree validation.
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False  # guarantees minimal number of edges for connectivity
        
        # Build undirected graph
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # undirected - add both directions
        
        visited = set()
        
        def dfs(node, parent):
            """
            DFS with parent tracking to detect cycles in undirected graph.
            
            Args:
                node: current node being visited
                parent: the node we came from (to avoid false cycle detection)
            
            Returns:
                False if cycle detected, True otherwise
            """
            if node in visited:
                return False  # found a cycle
            
            visited.add(node)
            
            for nei in graph[node]:
                # Skip the parent to avoid false cycle detection
                # (since edges are bidirectional, we'd see parent as neighbor)
                if nei != parent and not dfs(nei, node):
                    return False
            
            return True
        
        # Start DFS at any node (say 0) with no parent (-1)
        # Check if:
        # 1. No cycles exist (dfs returns True)
        # 2. All nodes are visited (len(visited) == n) - ensures connectivity
        return dfs(0, -1) and len(visited) == n


"""
✅ Explanation of Optimal Solution:

1. len(edges) == n - 1
   → A tree with n nodes MUST have exactly n-1 edges
   → This is a necessary condition for a tree
   → Catches cases with too many or too few edges early

2. DFS with parent tracking
   → Detects cycles safely for undirected edges
   → We skip the parent node when checking neighbors because in an undirected graph,
     the parent is always a neighbor, but going back to parent is not a cycle
   → If we visit a node that's already in visited (and it's not our parent), 
     we found a cycle

3. len(visited) == n
   → Ensures the graph is fully connected
   → If we can't reach all nodes from node 0, it's not a valid tree
   → Combined with n-1 edges check, this guarantees connectivity

Why parent tracking matters:
- In undirected graph: if we're at node A and came from node B,
  B is in A's neighbor list (because edges go both ways)
- Without parent tracking, we'd incorrectly detect a cycle: A→B→A
- By skipping parent, we only detect real cycles
"""


"""
🎯 Example Test Cases:

Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: True
Explanation: Forms a valid tree:
    0
   /|\
  1 2 3
 /
4

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: False
Explanation: Has a cycle: 1-2-3-1

Example 3:
Input: n = 5, edges = [[0,1],[0,2]]
Output: False
Explanation: Not connected (nodes 3 and 4 are isolated)

Example 4:
Input: n = 1, edges = []
Output: True
Explanation: Single node is a valid tree

Example 5:
Input: n = 4, edges = [[0,1],[2,3]]
Output: False
Explanation: Not connected (two separate components)
"""


"""
🔄 Alternative Solution: Union-Find (Disjoint Set)
===================================================

Another optimal approach using Union-Find data structure.
"""

class SolutionUnionFind:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Must have exactly n-1 edges
        if len(edges) != n - 1:
            return False
        
        # Initialize parent array
        parent = list(range(n))
        
        def find(x):
            """Find with path compression"""
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            """
            Union two sets.
            Returns False if they're already in the same set (cycle detected)
            """
            rootX = find(x)
            rootY = find(y)
            
            if rootX == rootY:
                return False  # Already connected - would create cycle
            
            parent[rootX] = rootY
            return True
        
        # Try to union all edges
        for u, v in edges:
            if not union(u, v):
                return False  # Cycle detected
        
        # If we have n-1 edges and no cycles, graph must be connected
        return True


"""
📊 Complexity Comparison:

DFS Solution:
- Time: O(n + e) where e = number of edges
- Space: O(n + e) for graph adjacency list + O(n) for recursion stack
- Pros: Intuitive, easy to understand
- Cons: Recursion depth could be an issue for very deep trees

Union-Find Solution:
- Time: O(n + e⋅α(n)) where α is inverse Ackermann (nearly O(1))
- Space: O(n) for parent array
- Pros: More space efficient, no recursion
- Cons: Slightly more complex to implement

Both are optimal for this problem. DFS is more commonly used.
"""
