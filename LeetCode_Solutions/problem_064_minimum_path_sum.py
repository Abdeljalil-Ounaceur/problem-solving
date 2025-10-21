"""
LeetCode Problem #64: Minimum Path Sum
Difficulty: Medium
Topics: Array, Dynamic Programming, Matrix

Problem Description:
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 200
"""

from typing import List


class Solution:
    """
    Initial Solution - In-place Dynamic Programming
    
    Approach:
    - Modify the grid in-place to store minimum path sums
    - Initialize first column: each cell = sum of all cells above it
    - Initialize first row: each cell = sum of all cells to its left
    - For remaining cells: add minimum of cell above or cell to the left
    
    Time Complexity: O(m*n) - visit each cell once
    Space Complexity: O(1) - modify grid in-place, no extra space
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Initialize first column (can only come from above)
        for i in range(1, len(grid)):
            grid[i][0] += grid[i-1][0]
        
        # Initialize first row (can only come from left)
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j-1]

        # Fill remaining cells: choose minimum path (from above or left)
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]


class SolutionCleaner:
    """
    Optimal Solution - Cleaner version with explicit dimensions
    
    Approach:
    - Same algorithm as initial solution but with better readability
    - Store dimensions m, n explicitly for clarity
    - Rest of the logic remains identical
    
    Time Complexity: O(m*n) - visit each cell once
    Space Complexity: O(1) - modify grid in-place, no extra space
    
    Key Insight:
    - At each cell (i,j), the minimum path sum is:
      grid[i][j] + min(minPathSum to cell above, minPathSum to cell left)
    - This is a classic DP problem where we build up the solution from base cases
    - Base cases: first row (can only go right) and first column (can only go down)
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Initialize first column
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        # Initialize first row
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]

        # Fill remaining cells
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]


# Test cases
if __name__ == "__main__":
    sol = Solution()
    sol_clean = SolutionCleaner()
    
    # Test case 1
    grid1 = [[1,3,1],[1,5,1],[4,2,1]]
    print(f"Test 1 - Initial: {sol.minPathSum([row[:] for row in grid1])}")  # Output: 7
    print(f"Test 1 - Cleaner: {sol_clean.minPathSum([row[:] for row in grid1])}")  # Output: 7
    
    # Test case 2
    grid2 = [[1,2,3],[4,5,6]]
    print(f"Test 2 - Initial: {sol.minPathSum([row[:] for row in grid2])}")  # Output: 12
    print(f"Test 2 - Cleaner: {sol_clean.minPathSum([row[:] for row in grid2])}")  # Output: 12
