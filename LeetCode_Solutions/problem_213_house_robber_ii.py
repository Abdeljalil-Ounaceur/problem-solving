"""
LeetCode Problem 213: House Robber II
Difficulty: Medium
Topics: Array, Dynamic Programming

Problem Description:
You are a professional robber planning to rob houses along a street. Each house has 
a certain amount of money stashed. All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. Meanwhile, adjacent houses 
have a security system connected, and it will automatically contact the police if two 
adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the 
maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), 
because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

Acceptance Rate: 44.1%
"""

from typing import List


class Solution:
    """
    Optimal Solution:
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    Approach: Two-pass Dynamic Programming
    - The key insight is that since houses are in a circle, we cannot rob both 
      the first and last house together
    - Solution: run the linear House Robber algorithm twice:
      1. Once excluding the last house (nums[:-1])
      2. Once excluding the first house (nums[1:])
    - Return the maximum of these two scenarios
    
    This reduces the circular problem to two linear House Robber problems,
    where we've already proven the optimal O(1) space solution works.
    
    Edge case: If there's only one house, we simply rob it.
    """
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev2 = prev1 = 0
        for n in nums[:-1]:  # Exclude last house
            prev2, prev1 = prev1, max(prev1, prev2 + n)
        max1 = prev1

        prev2 = prev1 = 0
        for n in nums[1:]:  # Exclude first house
            prev2, prev1 = prev1, max(prev1, prev2 + n)
        max2 = prev1

        return max(max1, max2)


class CleanerSolution:
    """
    Cleaner Solution:
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    Approach: Extract linear robbing logic into helper function
    - Same algorithm as Solution but with better code organization
    - Uses a helper function rob_linear() to avoid code duplication
    - Makes the solution more readable and maintainable
    
    This is the preferred implementation as it follows DRY (Don't Repeat Yourself)
    principle and makes the logic clearer.
    """
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses):
            prev2 = prev1 = 0
            for n in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + n)
            return prev1

        if len(nums) == 1:
            return nums[0]

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# Test cases
if __name__ == "__main__":
    solution = Solution()
    cleaner = CleanerSolution()
    
    test_cases = [
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),
        ([1, 2, 3], 3),
        ([1], 1),
        ([1, 2], 2),
        ([200, 3, 140, 20, 10], 340),  # Rob houses at index 0, 2 (200 + 140)
    ]
    
    print("Testing Optimal Solution:")
    for nums, expected in test_cases:
        result = solution.rob(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {nums}, Expected: {expected}, Got: {result}")
    
    print("\nTesting Cleaner Solution:")
    for nums, expected in test_cases:
        result = cleaner.rob(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {nums}, Expected: {expected}, Got: {result}")
