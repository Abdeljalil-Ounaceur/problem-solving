"""
LeetCode Problem #53: Maximum Subarray
Difficulty: Medium
Topics: Array, Dynamic Programming, Divide and Conquer

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's Algorithm - O(n) time, O(1) space
        The key insight is that at each position, we decide whether to:
        1. Start a new subarray from current element, or
        2. Extend the existing subarray by including current element
        """
        total_sum = nums[0]
        best = nums[0]
        i = 1
        N = len(nums)

        while i < N:
            if total_sum <= 0:
                # Start new subarray from current element
                total_sum = nums[i]
            else:
                # Extend existing subarray
                total_sum += nums[i]

            # Update the maximum sum seen so far
            best = max(best, total_sum)
            i += 1

        return best

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result1 = solution.maxSubArray(nums1)
    print(f"Test 1: nums={nums1} -> {result1}")  # Expected: 6
    
    # Test case 2
    nums2 = [1]
    result2 = solution.maxSubArray(nums2)
    print(f"Test 2: nums={nums2} -> {result2}")  # Expected: 1
    
    # Test case 3
    nums3 = [5, 4, -1, 7, 8]
    result3 = solution.maxSubArray(nums3)
    print(f"Test 3: nums={nums3} -> {result3}")  # Expected: 23
    
    # Additional test cases
    nums4 = [-1, -2, -3, -4]  # All negative
    result4 = solution.maxSubArray(nums4)
    print(f"Test 4: nums={nums4} -> {result4}")  # Expected: -1
    
    nums5 = [2, -1, 2, 3, 4, -5]
    result5 = solution.maxSubArray(nums5)
    print(f"Test 5: nums={nums5} -> {result5}")  # Expected: 10
