"""
LeetCode Problem #33: Search in Rotated Sorted Array
Difficulty: Medium
Topics: Array, Binary Search

Problem:
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly left rotated at an unknown 
index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index 
of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique.
- nums is an ascending array that is possibly rotated.
- -10^4 <= target <= 10^4
"""

from typing import List

class Solution:
    """
    Initial Solution (Unoptimized):
    This solution handles the rotation cases with multiple conditional checks.
    While correct, the logic is more complex and harder to follow.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    def search_unoptimized(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            
            if target > nums[middle]:
                if target <= nums[right] or nums[middle] > nums[right]:
                    left = middle + 1
                elif nums[right] < nums[left]:
                    right = middle - 1
                else:
                    return -1
            else:
                if target >= nums[left] or nums[middle] < nums[left]:
                    right = middle - 1
                elif nums[left] > nums[right]:
                    left = middle + 1       
                else:
                    return -1
        
        return -1

    """
    Optimal Solution:
    The key insight is to identify which half of the array is sorted, then check if the
    target lies within that sorted portion.
    
    At any point during binary search, at least one half (left or right) must be sorted.
    - If left half is sorted (nums[left] <= nums[mid]):
      - Check if target is in the sorted left half
      - If yes, search left; otherwise search right
    - If right half is sorted (nums[mid] < nums[right]):
      - Check if target is in the sorted right half
      - If yes, search right; otherwise search left
    
    Time Complexity: O(log n) - Binary search
    Space Complexity: O(1) - Constant space
    """
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target is in the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                # Check if target is in the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    print(f"Test 1: nums = {nums1}, target = {target1}")
    print(f"Output: {solution.search(nums1, target1)}")  # Expected: 4
    
    # Test case 2
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    print(f"\nTest 2: nums = {nums2}, target = {target2}")
    print(f"Output: {solution.search(nums2, target2)}")  # Expected: -1
    
    # Test case 3
    nums3 = [1]
    target3 = 0
    print(f"\nTest 3: nums = {nums3}, target = {target3}")
    print(f"Output: {solution.search(nums3, target3)}")  # Expected: -1
    
    # Test case 4 - No rotation
    nums4 = [1, 2, 3, 4, 5, 6, 7]
    target4 = 5
    print(f"\nTest 4: nums = {nums4}, target = {target4}")
    print(f"Output: {solution.search(nums4, target4)}")  # Expected: 4
    
    # Test case 5 - Rotation at the end
    nums5 = [3, 1]
    target5 = 1
    print(f"\nTest 5: nums = {nums5}, target = {target5}")
    print(f"Output: {solution.search(nums5, target5)}")  # Expected: 1
