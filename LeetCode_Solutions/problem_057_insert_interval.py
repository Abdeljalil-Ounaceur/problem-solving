"""
LeetCode Problem #57: Insert Interval
Difficulty: Medium
Topics: Array, Sorting

Problem Description:
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti 
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5

Time Complexity: O(n) - single pass through intervals
Space Complexity: O(n) - for the result array
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Optimized solution using three-phase approach:
        1. Add all intervals that end before newInterval starts
        2. Merge all overlapping intervals with newInterval
        3. Add all intervals that start after newInterval ends
        """
        res = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                # current interval ends before new interval starts
                res.append(interval)
            elif interval[0] > newInterval[1]:
                # current interval starts after new interval ends
                res.append(newInterval)
                newInterval = interval  # shift focus to remaining intervals
            else:
                # overlap → merge
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        res.append(newInterval)
        return res


class SolutionUnoptimized:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Initial unoptimized solution with more complex logic
        """
        if intervals == []:
            return [newInterval]
        new_intervals = []
        inserted = False

        for interval in intervals:
            if (interval[0] <= newInterval[1] and newInterval[0] <= interval[1]):
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
            else:
                if not inserted and newInterval[0] <= interval[1]:
                    new_intervals += sorted([newInterval, interval], key=lambda x: x[0])
                    inserted = True
                else:
                    new_intervals.append(interval)
        if not inserted:
            new_intervals.append(newInterval)
        return new_intervals


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution_unopt = SolutionUnoptimized()
    
    # Test case 1
    intervals1 = [[1,3],[6,9]]
    newInterval1 = [2,5]
    result1 = solution.insert(intervals1, newInterval1)
    result1_unopt = solution_unopt.insert([[1,3],[6,9]], [2,5])
    print(f"Test 1: {intervals1}, {newInterval1} -> {result1}")
    print(f"Test 1 (unopt): -> {result1_unopt}")
    # Expected: [[1,5],[6,9]]
    
    # Test case 2
    intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval2 = [4,8]
    result2 = solution.insert(intervals2, newInterval2)
    result2_unopt = solution_unopt.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
    print(f"Test 2: {intervals2}, {newInterval2} -> {result2}")
    print(f"Test 2 (unopt): -> {result2_unopt}")
    # Expected: [[1,2],[3,10],[12,16]]
    
    # Additional test cases
    intervals3 = []
    newInterval3 = [5,7]
    result3 = solution.insert(intervals3, newInterval3)
    print(f"Test 3: {intervals3}, {newInterval3} -> {result3}")
    # Expected: [[5,7]]
    
    intervals4 = [[1,5]]
    newInterval4 = [2,3]
    result4 = solution.insert(intervals4, newInterval4)
    print(f"Test 4: {intervals4}, {newInterval4} -> {result4}")
    # Expected: [[1,5]]
    
    intervals5 = [[1,5]]
    newInterval5 = [6,8]
    result5 = solution.insert(intervals5, newInterval5)
    print(f"Test 5: {intervals5}, {newInterval5} -> {result5}")
    # Expected: [[1,5],[6,8]]
