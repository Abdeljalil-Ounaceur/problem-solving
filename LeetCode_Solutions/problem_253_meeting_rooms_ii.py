"""
LeetCode Problem #253: Meeting Rooms II

Given an array of meeting time interval objects consisting of start and end times 
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number 
of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.

Example 1:
Input: intervals = [(0,40),(5,10),(15,20)]
Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:
Input: intervals = [(4,9)]
Output: 1

Constraints:
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from typing import List
import heapq


# My initial solution
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: 
            return 0
        
        # Sort intervals by start time
        intervals.sort(key=lambda x: x.start)
        
        # Track end times of meetings in each room
        ends = [intervals[0].end]
        
        for i in range(1, len(intervals)):
            merged = False
            # Check if any room is available (its meeting has ended)
            for j in range(len(ends)):
                if ends[j] <= intervals[i].start:
                    # Reuse this room - update its end time
                    ends[j] = intervals[i].end
                    merged = True
                    break
                    
            if not merged:
                # Need a new room
                ends.append(intervals[i].end)
                
        return len(ends)


# Optimal solution using heap
class SolutionOptimal:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        # Sort by start time
        intervals.sort(key=lambda x: x.start)
        
        # Min-heap of meeting end times
        heap = [intervals[0].end]
        
        for i in range(1, len(intervals)):
            # If the room with the earliest end time is free, reuse it
            if heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
        
        return len(heap)


# Another optimal but also elegant solution using two pointers
class SolutionOptimal2:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        # Separate and sort start and end times
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        
        s = e = 0  # pointers for start and end
        count = max_rooms = 0
        
        # Iterate while we have unprocessed start times
        while s < len(intervals):
            if starts[s] < ends[e]:
                # A new meeting starts before the earliest one ends → need a room
                count += 1
                max_rooms = max(max_rooms, count)
                s += 1
            else:
                # A meeting ended before the next one starts → free a room
                count -= 1
                e += 1
        
        return max_rooms


# Test cases
if __name__ == "__main__":
    # Helper class for testing
    class Interval:
        def __init__(self, start, end):
            self.start = start
            self.end = end
    
    # Example 1
    intervals1 = [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
    sol = Solution()
    print(f"Example 1: {sol.minMeetingRooms(intervals1)}")  # Expected: 2
    
    sol_opt = SolutionOptimal()
    print(f"Example 1 (Optimal): {sol_opt.minMeetingRooms(intervals1)}")  # Expected: 2
    
    sol_opt2 = SolutionOptimal2()
    print(f"Example 1 (Optimal 2): {sol_opt2.minMeetingRooms(intervals1)}")  # Expected: 2
    
    # Example 2
    intervals2 = [Interval(4, 9)]
    print(f"Example 2: {sol.minMeetingRooms(intervals2)}")  # Expected: 1
    print(f"Example 2 (Optimal): {sol_opt.minMeetingRooms(intervals2)}")  # Expected: 1
    print(f"Example 2 (Optimal 2): {sol_opt2.minMeetingRooms(intervals2)}")  # Expected: 1

