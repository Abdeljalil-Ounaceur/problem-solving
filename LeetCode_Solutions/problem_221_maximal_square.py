"""
221. Maximal Square
Solved
Medium
Topics: Array, Dynamic Programming, Matrix

Given an m x n binary matrix filled with 0's and 1's, find the largest square 
containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 300
- matrix[i][j] is '0' or '1'.
"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Initial solution using in-place DP modification.
        
        Approach:
        - Convert string matrix to integers for easier manipulation
        - Initialize max_square from first row and column
        - For each cell (i,j), if it's 1, set it to min of three neighbors + 1
        - The value at each cell represents the side length of largest square ending there
        - Track maximum side length and return its square
        
        Time Complexity: O(m * n) where m is rows and n is columns
        Space Complexity: O(m * n) for converting matrix to integers
        """
        matrix = [[int(c) for c in row] for row in matrix]
        
        max_square = max(matrix[0] + [row[0] for row in matrix])

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != 0:
                    matrix[i][j] = min([matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]]) + 1
                    max_square = max(max_square, matrix[i][j])

        return max_square**2


class SolutionOptimal:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Optimal solution using space-optimized DP with two 1D arrays.
        
        Approach:
        - Use two 1D arrays (prev and curr) instead of 2D DP table
        - prev represents the previous row's DP values
        - curr represents the current row being computed
        - For each cell, if it's "1", compute min of three neighbors + 1
        - After processing each row, swap prev and curr
        - Track maximum side length and return its square
        
        Key Insight:
        - We only need the previous row to compute the current row
        - This reduces space complexity from O(m*n) to O(n)
        - The DP recurrence: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        Time Complexity: O(m * n) where m is rows and n is columns
        Space Complexity: O(n) for the two 1D arrays
        """
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        prev = [0] * (cols + 1)  # Extra padding to avoid index checks
        max_side = 0

        for i in range(1, rows + 1):
            curr = [0] * (cols + 1)
            for j in range(1, cols + 1):
                if matrix[i-1][j-1] == "1":
                    # Current square side = min of three neighbors + 1
                    curr[j] = min(prev[j], curr[j-1], prev[j-1]) + 1
                    max_side = max(max_side, curr[j])
            prev = curr

        return max_side ** 2


# Test cases
if __name__ == "__main__":
    solution = Solution()
    optimal = SolutionOptimal()
    
    # Test case 1
    matrix1 = [["1","0","1","0","0"],
               ["1","0","1","1","1"],
               ["1","1","1","1","1"],
               ["1","0","0","1","0"]]
    print(f"Test 1: {solution.maximalSquare(matrix1)}")  # Expected: 4
    print(f"Test 1 (Optimal): {optimal.maximalSquare(matrix1)}")  # Expected: 4
    
    # Test case 2
    matrix2 = [["0","1"],["1","0"]]
    print(f"Test 2: {solution.maximalSquare(matrix2)}")  # Expected: 1
    print(f"Test 2 (Optimal): {optimal.maximalSquare(matrix2)}")  # Expected: 1
    
    # Test case 3
    matrix3 = [["0"]]
    print(f"Test 3: {solution.maximalSquare(matrix3)}")  # Expected: 0
    print(f"Test 3 (Optimal): {optimal.maximalSquare(matrix3)}")  # Expected: 0
