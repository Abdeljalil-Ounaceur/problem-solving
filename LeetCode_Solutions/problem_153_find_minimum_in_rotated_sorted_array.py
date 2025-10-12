"""
LeetCode Problem 153: Find Minimum in Rotated Sorted Array
Difficulty: Medium
Topics: Array, Binary Search

Problem Description:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the 
array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.
- nums is sorted and rotated between 1 and n times.
"""

from typing import List


# Initial Solution - Works but could be clearer
class Solution_Initial:
    """
    Initial working solution with more complex conditional logic.
    
    Approach:
    - Uses binary search with left <= right condition
    - Checks if middle == left as a base case
    - Compares middle with both left and right to determine direction
    
    Time Complexity: O(log n) - binary search
    Space Complexity: O(1) - constant extra space
    
    The logic is a bit convoluted with multiple conditions checking both left and right.
    """
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if middle == left:
                return min(nums[left], nums[right])
            elif nums[middle] > nums[left]:
                if nums[middle] < nums[right]:
                    return nums[left]
                else:
                    left = middle
            else:
                right = middle


# Optimal Solution - Cleaner and more intuitive
class Solution:
    """
    Optimal binary search solution with simplified logic.
    
    Key Insight:
    - In a rotated sorted array, the minimum element is at the rotation point
    - Compare mid with right to determine which half contains the minimum
    - If nums[mid] > nums[right]: minimum must be in right half (mid+1 to right)
    - If nums[mid] <= nums[right]: minimum is in left half including mid (left to mid)
    
    Why compare with right instead of left?
    - Comparing with right gives us clear information about where the rotation point is
    - If mid > right, we know rotation happened and minimum is to the right
    - If mid <= right, this portion is sorted and minimum could be mid or to the left
    
    Time Complexity: O(log n) - binary search halves search space each iteration
    Space Complexity: O(1) - only uses a few pointers
    
    The loop continues while left < right (not <=), ensuring we stop when left == right.
    At that point, left (or right) points to the minimum element.
    """
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # Minimum is in the right half
                # mid cannot be minimum since it's greater than right
                left = mid + 1
            else:
                # Minimum is in the left half (including mid)
                # mid could be the minimum, so we keep it in the search space
                right = mid
                
        return nums[left]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution_initial = Solution_Initial()
    
    # Test case 1
    nums1 = [3, 4, 5, 1, 2]
    assert solution.findMin(nums1) == 1
    assert solution_initial.findMin(nums1) == 1
    print(f"Test 1 passed: {nums1} -> 1")
    
    # Test case 2
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    assert solution.findMin(nums2) == 0
    assert solution_initial.findMin(nums2) == 0
    print(f"Test 2 passed: {nums2} -> 0")
    
    # Test case 3
    nums3 = [11, 13, 15, 17]
    assert solution.findMin(nums3) == 11
    assert solution_initial.findMin(nums3) == 11
    print(f"Test 3 passed: {nums3} -> 11")
    
    # Additional edge case: single element
    nums4 = [1]
    assert solution.findMin(nums4) == 1
    assert solution_initial.findMin(nums4) == 1
    print(f"Test 4 passed: {nums4} -> 1")
    
    # Additional edge case: two elements
    nums5 = [2, 1]
    assert solution.findMin(nums5) == 1
    assert solution_initial.findMin(nums5) == 1
    print(f"Test 5 passed: {nums5} -> 1")
    
    print("\nAll test cases passed!")
