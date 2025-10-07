"""
LeetCode Problem 417: Pacific Atlantic Water Flow
Difficulty: Medium
Topics: Array, Depth-First Search, Breadth-First Search, Matrix

Note: I couldn't solve this one until I saw the solution so meh.

Problem Description:
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the 
island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix 
heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly 
north, south, east, and west if the neighboring cell's height is less than or equal to the 
current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water 
can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

Constraints:
- m == heights.length
- n == heights[r].length
- 1 <= m, n <= 200
- 0 <= heights[r][c] <= 10^5

Time Complexity: O(m*n) where m and n are dimensions of the grid (each cell visited at most twice)
Space Complexity: O(m*n) for the reachable matrices and BFS queue

Key Insight:
Instead of checking if water can flow FROM each cell TO the oceans (complex), 
reverse the problem: check which cells the oceans can reach flowing UPWARD.
Then find the intersection of cells reachable by both oceans.
"""

from collections import deque
from typing import List


class Solution:
    """
    OPTIMAL SOLUTION: Reverse BFS from Ocean Borders
    
    Strategy:
    1. Start BFS from all Pacific Ocean border cells (top row, left column)
    2. Start BFS from all Atlantic Ocean border cells (bottom row, right column)
    3. In reverse flow, water flows from lower to higher or equal cells
    4. Find intersection of cells reachable by both oceans
    
    Why this works:
    - If water can flow from cell A to ocean, then ocean can "flow back" to cell A
    - This reversal simplifies the problem from exponential to linear time
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        
        # reachable_p[r][c] = True if (r,c) can reach Pacific side (via reverse BFS/DFS)
        # reachable_a[r][c] = True if (r,c) can reach Atlantic side
        reachable_p = [[False] * n for _ in range(m)]
        reachable_a = [[False] * n for _ in range(m)]
        
        # Directions (4 neighbors)
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def bfs(starting_cells, reachable):
            """BFS from all starting_cells, marking in reachable matrix."""
            q = deque(starting_cells)
            for (r, c) in starting_cells:
                reachable[r][c] = True
            
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    # Flow upward: neighbor must be >= current height
                    if (0 <= nr < m and 0 <= nc < n
                        and not reachable[nr][nc]
                        and heights[nr][nc] >= heights[r][c]):
                        reachable[nr][nc] = True
                        q.append((nr, nc))
        
        # Initialize Pacific starting border cells (top row + left column)
        pac_starts = []
        for r in range(m):
            pac_starts.append((r, 0))  # Left column
        for c in range(n):
            pac_starts.append((0, c))  # Top row
        
        # Initialize Atlantic starting border cells (bottom row + right column)
        atl_starts = []
        for r in range(m):
            atl_starts.append((r, n-1))  # Right column
        for c in range(n):
            atl_starts.append((m-1, c))  # Bottom row
        
        # BFS from both sides
        bfs(pac_starts, reachable_p)
        bfs(atl_starts, reachable_a)
        
        # Collect cells reachable by both
        result = []
        for r in range(m):
            for c in range(n):
                if reachable_p[r][c] and reachable_a[r][c]:
                    result.append([r, c])
        return result


# ============================================================================
# MY INITIAL ATTEMPT (Doesn't Work Correctly)
# ============================================================================
"""
Issues with my initial approach:
1. DFS from each cell trying to reach both oceans is exponentially complex
2. Memoization is tricky because paths are interdependent
3. The visited set handling is problematic - it's passed recursively but 
   needs to be managed per-path, not globally
4. Checking tracker[(row,col)] is not None won't work properly because
   the memoization doesn't account for different paths
"""

from typing import *
from collections import defaultdict

class SolutionInitial:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        tracker = defaultdict(lambda:None)
        
        def dfs(row, col, tracker, val, visited):
            if row < 0 or col < 0:
                return (True, False)  # Reached Pacific
            if row >= len(heights) or col >= len(heights[0]):
                return (False, True)  # Reached Atlantic
            
            if val and val < heights[row][col]:
                return (False, False)  # Can't flow upward

            if tracker[(row, col)] is not None:
                return tracker[(row, col)]

            pacific = atlantic = False
            visited.add((row, col))

            for (i, j) in (0, -1), (-1, 0), (1, 0), (0, 1):
                if (row + i, col + j) in visited:
                    continue
                p, a = dfs(row + i, col + j, tracker, heights[row][col], visited)
                
                pacific = pacific or p
                atlantic = atlantic or a
            
            tracker[(row, col)] = (pacific, atlantic)
            return (pacific, atlantic)

        success = []

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                res = tracker[(i, j)] or dfs(i, j, tracker, None, set())
                if all(res):
                    success.append([i, j])

        return success


# ============================================================================
# Testing
# ============================================================================
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    heights1 = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    result1 = solution.pacificAtlantic(heights1)
    print(f"Test 1: {result1}")
    # Expected: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    
    # Test Case 2
    heights2 = [[1]]
    result2 = solution.pacificAtlantic(heights2)
    print(f"Test 2: {result2}")
    # Expected: [[0,0]]
    
    # Test Case 3: Edge case with all same heights
    heights3 = [[1,1],[1,1]]
    result3 = solution.pacificAtlantic(heights3)
    print(f"Test 3: {result3}")
    # Expected: [[0,0],[0,1],[1,0],[1,1]] (all cells can reach both oceans)
