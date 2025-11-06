"""
LeetCode Problem #252: Meeting Rooms
Difficulty: Easy
Topics: Array, Sorting, Intervals

Problem Description:
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a 
person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Explanation: The person cannot attend all meetings because meetings [0,30] and [5,10] overlap.

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
Explanation: The person can attend all meetings because no meetings overlap.

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti < endi <= 10^6

Time Complexity: O(n log n) - due to sorting
Space Complexity: O(1) - excluding the space for sorting (which can be O(n) depending on implementation)
"""

from typing import List

# Definition of Interval (as used in LeetCode):
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        My solution: Sort intervals by start time, then check if any meeting overlaps with the previous one.
        """
        intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True


class SolutionOptimal:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        Optimal solution: Same approach but using .sort() method instead of sorted().
        """
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True


# Alternative solution using list of lists instead of Interval objects
class SolutionList:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Solution for the variant where intervals are given as list of lists.
        """
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution_optimal = SolutionOptimal()
    solution_list = SolutionList()
    
    # Test case 1: Overlapping meetings
    intervals1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    result1 = solution.canAttendMeetings(intervals1)
    print(f"Test 1: {[(i.start, i.end) for i in intervals1]} -> {result1}")
    # Expected: False (meetings [0,30] and [5,10] overlap)
    
    # Test case 2: Non-overlapping meetings
    intervals2 = [Interval(7, 10), Interval(2, 4)]
    result2 = solution.canAttendMeetings(intervals2)
    print(f"Test 2: {[(i.start, i.end) for i in intervals2]} -> {result2}")
    # Expected: True (no overlapping meetings)
    
    # Test case 3: Single meeting
    intervals3 = [Interval(1, 3)]
    result3 = solution.canAttendMeetings(intervals3)
    print(f"Test 3: {[(i.start, i.end) for i in intervals3]} -> {result3}")
    # Expected: True
    
    # Test case 4: Empty list
    intervals4 = []
    result4 = solution.canAttendMeetings(intervals4)
    print(f"Test 4: {intervals4} -> {result4}")
    # Expected: True (no meetings to conflict)
    
    # Test case 5: Meetings that touch at endpoints (non-overlapping)
    intervals5 = [Interval(1, 2), Interval(2, 3)]
    result5 = solution.canAttendMeetings(intervals5)
    print(f"Test 5: {[(i.start, i.end) for i in intervals5]} -> {result5}")
    # Expected: True (meetings that only touch at a point are considered non-overlapping)
    
    # Test case 6: Using list of lists format
    intervals6 = [[0, 30], [5, 10], [15, 20]]
    result6 = solution_list.canAttendMeetings(intervals6)
    print(f"Test 6 (list format): {intervals6} -> {result6}")
    # Expected: False

