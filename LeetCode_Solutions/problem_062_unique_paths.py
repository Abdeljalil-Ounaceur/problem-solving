"""
LeetCode Problem 62: Unique Paths
Difficulty: Medium
Topics: Math, Dynamic Programming, Combinatorics

Problem Description:
There is a robot on an m x n grid. The robot is initially located at the top-left 
corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner 
(i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any 
point in time.

Given the two integers m and n, return the number of possible unique paths that 
the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the 
bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
1 <= m, n <= 100
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Initial Solution: 2D DP Grid
        
        Approach:
        - Create a 2D grid where grid[i][j] represents the number of unique paths
          to reach cell (i, j) from (0, 0)
        - Initialize first row and first column to 1 (only one way to reach them)
        - For each cell, the number of paths = paths from above + paths from left
        - Return grid[m-1][n-1]
        
        Time Complexity: O(m * n) - visit each cell once
        Space Complexity: O(m * n) - for the 2D grid
        """
        grid = [[0]*n for _ in range(m)]

        # Initialize first row
        for i in range(n):
            grid[0][i] = 1
        
        # Initialize first column
        for i in range(m):
            grid[i][0] = 1
        
        # Fill the grid using DP relation
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i][j-1] + grid[i-1][j]
            
        return grid[m-1][n-1]


class OptimalSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Optimal Solution: 1D DP Array (Space Optimized)
        
        Approach:
        - Instead of maintaining a full 2D grid, use a single row array
        - Initialize row with all 1s (representing the first row)
        - For each subsequent row, update the array in-place
        - At each position j, row[j] = row[j] (from above) + row[j-1] (from left)
        - The key insight: we only need the previous row to compute the current row
        
        Time Complexity: O(m * n) - still visit each cell conceptually
        Space Complexity: O(n) - only store one row at a time
        
        Why this works:
        - row[j] initially contains the value from the previous row (above)
        - row[j-1] contains the updated value from the current row (left)
        - By updating in-place left to right, we maintain both values we need
        """
        row = [1] * n
        
        for _ in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]
        
        return row[-1]
