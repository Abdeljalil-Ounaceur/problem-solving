"""
LeetCode Problem #238: Product of Array Except Self
Difficulty: Medium
Topics: Array, Prefix Sum

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # First pass: calculate left products
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]
        
        # Second pass: calculate right products and multiply with left products
        right = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        
        return answer

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 4]
    result1 = solution.productExceptSelf(nums1)
    print(f"Test 1: nums={nums1} -> {result1}")  # Expected: [24, 12, 8, 6]
    
    # Test case 2
    nums2 = [-1, 1, 0, -3, 3]
    result2 = solution.productExceptSelf(nums2)
    print(f"Test 2: nums={nums2} -> {result2}")  # Expected: [0, 0, 9, 0, 0]
    
    # Additional test case
    nums3 = [2, 3, 4, 5]
    result3 = solution.productExceptSelf(nums3)
    print(f"Test 3: nums={nums3} -> {result3}")  # Expected: [60, 40, 30, 24]
