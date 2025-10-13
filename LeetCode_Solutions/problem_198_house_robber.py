"""
LeetCode Problem 198: House Robber
Difficulty: Medium
Topics: Array, Dynamic Programming

Problem Description:
You are a professional robber planning to rob houses along a street. Each house has 
a certain amount of money stashed, the only constraint stopping you from robbing each 
of them is that adjacent houses have security systems connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the 
maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

Acceptance Rate: 52.6%
"""

from typing import List


class Solution:
    """
    Initial Solution:
    - Time Complexity: O(n)
    - Space Complexity: O(n) - modifies input array with padding
    
    Approach: Dynamic Programming with array padding
    - Pads array with three zeros at the beginning
    - For each house i, adds maximum of (i-2) or (i-3) to current value
    - Returns maximum of last two elements
    
    This works but uses extra space and modifies the input array.
    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = [0]*3 + nums
        for i in range(3, len(nums)):
            nums[i] += max(nums[i-3], nums[i-2])
        
        return max(nums[-2:])


class OptimalSolution:
    """
    Optimal Solution:
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    Approach: Space-optimized Dynamic Programming
    - Uses only two variables (prev2, prev1) to track previous states
    - For each house, calculates max of:
      1. Skip current house: prev1
      2. Rob current house: prev2 + current value
    - Updates both pointers in a single line using tuple unpacking
    
    Key Insight:
    At any house, the decision is:
    - If we rob it: we get current value + max money from houses up to i-2
    - If we skip it: we keep max money from houses up to i-1
    
    This is a classic DP optimization where we only need the last two states,
    similar to Fibonacci sequence calculation.
    """
    def rob(self, nums: List[int]) -> int:
        prev2 = prev1 = 0
        for n in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + n)
        return prev1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    optimal = OptimalSolution()
    
    test_cases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([5, 3, 4, 11, 2], 16),  # Rob houses at index 0, 3 (5 + 11)
        ([1], 1),
        ([2, 1], 2),
    ]
    
    print("Testing Initial Solution:")
    for nums, expected in test_cases:
        result = solution.rob(nums.copy())  # Use copy to avoid mutation
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {nums}, Expected: {expected}, Got: {result}")
    
    print("\nTesting Optimal Solution:")
    for nums, expected in test_cases:
        result = optimal.rob(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {nums}, Expected: {expected}, Got: {result}")
