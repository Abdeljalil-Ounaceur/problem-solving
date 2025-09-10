"""
LeetCode Problem #56: Merge Intervals
Difficulty: Medium
Topics: Array, Sorting

Problem Description:
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping 
intervals, and return an array of the non-overlapping intervals that cover all the 
intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

Constraints:
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4

Time Complexity: O(n log n) - due to sorting
Space Complexity: O(1) - excluding the output array
"""


class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        # Step 1: sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:  # overlap
                last[1] = max(last[1], current[1])  # merge
            else:
                merged.append(current)
        
        return merged


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    result1 = solution.merge(intervals1)
    print(f"Test 1: {intervals1} -> {result1}")
    # Expected: [[1,6],[8,10],[15,18]]
    
    # Test case 2
    intervals2 = [[1,4],[4,5]]
    result2 = solution.merge(intervals2)
    print(f"Test 2: {intervals2} -> {result2}")
    # Expected: [[1,5]]
    
    # Test case 3
    intervals3 = [[4,7],[1,4]]
    result3 = solution.merge(intervals3)
    print(f"Test 3: {intervals3} -> {result3}")
    # Expected: [[1,7]]
    
    # Additional test cases
    intervals4 = [[1,3]]
    result4 = solution.merge(intervals4)
    print(f"Test 4: {intervals4} -> {result4}")
    # Expected: [[1,3]]
    
    intervals5 = [[1,4],[2,3]]
    result5 = solution.merge(intervals5)
    print(f"Test 5: {intervals5} -> {result5}")
    # Expected: [[1,4]]
