"""
LeetCode Problem 704: Binary Search
Difficulty: Easy
Topics: Array, Binary Search

Problem:
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index.
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique.
- nums is sorted in ascending order.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Classic binary search implementation.
        
        Approach:
        - Maintain two pointers: left and right
        - Calculate middle index and compare with target
        - If middle element equals target, return index
        - If middle element is less than target, search right half
        - If middle element is greater than target, search left half
        - Continue until left > right (target not found)
        
        Time Complexity: O(log n) - halving search space each iteration
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            nums: Sorted array of integers
            target: Integer to search for
            
        Returns:
            int: Index of target if found, -1 otherwise
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1


# Alternative Solution: Recursive Binary Search
class SolutionRecursive:
    def search(self, nums: List[int], target: int) -> int:
        """
        Recursive binary search implementation.
        
        Time Complexity: O(log n)
        Space Complexity: O(log n) - recursion stack
        """
        def binary_search(left: int, right: int) -> int:
            if left > right:
                return -1
            
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            else:
                return binary_search(left, mid - 1)
        
        return binary_search(0, len(nums) - 1)


# Alternative Solution: Using Python's bisect module
class SolutionBisect:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search using Python's built-in bisect module.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        import bisect
        
        idx = bisect.bisect_left(nums, target)
        if idx < len(nums) and nums[idx] == target:
            return idx
        return -1
