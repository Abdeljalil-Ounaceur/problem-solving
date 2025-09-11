"""
LeetCode Problem 435: Non-overlapping Intervals
Difficulty: Medium
Topics: Array, Dynamic Programming, Greedy, Sorting

Problem Description:
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest 
of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. 
For example, [1, 2] and [2, 3] are non-overlapping.

Examples:
Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= starti < endi <= 5 * 10^4
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Initial solution: Sort by start time and greedily remove overlapping intervals.
        
        Time Complexity: O(n log n) for sorting
        Space Complexity: O(1) extra space
        
        Approach:
        1. Sort intervals by start time
        2. Keep track of reference interval
        3. For each overlapping interval, remove the one with later end time
        4. Count total removals
        """
        num_to_remove = 0
        intervals.sort(key=lambda x: x[0])

        if intervals == []:
            return 0
        
        reference = intervals[0]
        
        for interval in intervals[1:]:
            if interval[0] < reference[1]:  # overlap detected
                num_to_remove += 1
                # Keep the interval with earlier end time
                if interval[1] <= reference[1]:
                    reference = interval
            else:
                reference = interval
        return num_to_remove


class OptimalSolution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Optimal solution: Sort by end time and use greedy approach.
        
        Time Complexity: O(n log n) for sorting
        Space Complexity: O(1) extra space
        
        Approach:
        1. Sort intervals by end time (key insight!)
        2. Always keep the interval that ends earliest
        3. This maximizes the number of non-overlapping intervals we can keep
        4. Count overlapping intervals that need to be removed
        
        Why sorting by end time is optimal:
        - By always choosing the interval that ends earliest, we leave maximum
          room for future intervals
        - This greedy choice leads to the optimal solution
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])  # sort by end time
        count = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:  # overlap detected
                count += 1
            else:
                prev_end = end
        return count


# Test cases
def test_solutions():
    solution = Solution()
    optimal = OptimalSolution()
    
    test_cases = [
        [[1,2],[2,3],[3,4],[1,3]],  # Expected: 1
        [[1,2],[1,2],[1,2]],        # Expected: 2
        [[1,2],[2,3]],              # Expected: 0
        [[1,100],[11,22],[1,11],[2,12]]  # Expected: 2
    ]
    
    for i, intervals in enumerate(test_cases):
        result1 = solution.eraseOverlapIntervals(intervals.copy())
        result2 = optimal.eraseOverlapIntervals(intervals.copy())
        print(f"Test case {i+1}: {intervals}")
        print(f"Initial solution: {result1}")
        print(f"Optimal solution: {result2}")
        print(f"Results match: {result1 == result2}")
        print()


if __name__ == "__main__":
    test_solutions()
