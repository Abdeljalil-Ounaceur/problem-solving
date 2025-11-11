"""
LeetCode Problem #378: Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each of the rows and columns is sorted in ascending order, 
return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n²).

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 300
-10^9 <= matrix[i][j] <= 10^9
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n²

Follow up:
Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
"""

from typing import List


# Optimal solution using binary search on answer space
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # n = number of rows (matrix is n x n)
        n = len(matrix)

        # Helper function: counts how many numbers in the matrix are <= x
        def count_less_equal(x):
            count = 0

            # Start from bottom-left corner of the matrix
            # (because from there, you can move up or right based on comparisons)
            row = n - 1
            col = 0

            # While we're inside the matrix boundaries
            while row >= 0 and col < n:
                if matrix[row][col] <= x:
                    # All elements above this one in the same column are <= x
                    # So add (row + 1) to the count
                    count += row + 1

                    # Move right to the next column
                    col += 1
                else:
                    # If current element > x, move up to a smaller value
                    row -= 1

            # Return how many numbers <= x
            return count

        # Binary search range = smallest and largest values in the matrix
        lo, hi = matrix[0][0], matrix[-1][-1]

        # Binary search until the range converges
        while lo < hi:
            mid = (lo + hi) // 2  # midpoint value between lo and hi

            # Count how many elements are <= mid
            if count_less_equal(mid) < k:
                # If there are fewer than k elements <= mid,
                # then the k-th smallest must be larger
                lo = mid + 1
            else:
                # Otherwise, it could be mid or smaller
                hi = mid

        # When lo == hi, it's the k-th smallest element
        return lo


# Alternative solution using heap (O(k log n) time, O(n) space)
# Note: This doesn't meet the memory complexity requirement for large k
import heapq


class SolutionHeap:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        # Min heap: (value, row, col)
        heap = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(heap)
        
        # Extract k-1 smallest elements
        for _ in range(k - 1):
            val, row, col = heapq.heappop(heap)
            # If there's a next element in this row, add it to heap
            if col + 1 < n:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
        
        # The k-th smallest is at the top of the heap
        return heap[0][0]


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    matrix1 = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k1 = 8
    result1 = sol.kthSmallest(matrix1, k1)
    print(f"Example 1: {result1}")  # Expected: 13
    print(f"Explanation: Elements sorted: {sorted([1,5,9,10,11,12,13,13,15])}, 8th smallest = {result1}")
    
    # Example 2
    matrix2 = [[-5]]
    k2 = 1
    result2 = sol.kthSmallest(matrix2, k2)
    print(f"Example 2: {result2}")  # Expected: -5
    
    # Additional test case
    matrix3 = [[1, 2], [1, 3]]
    k3 = 2
    result3 = sol.kthSmallest(matrix3, k3)
    print(f"Additional test: {result3}")  # Expected: 1
    
    # Test with heap solution
    sol_heap = SolutionHeap()
    print(f"\nHeap solution Example 1: {sol_heap.kthSmallest(matrix1, k1)}")  # Expected: 13
    print(f"Heap solution Example 2: {sol_heap.kthSmallest(matrix2, k2)}")  # Expected: -5

