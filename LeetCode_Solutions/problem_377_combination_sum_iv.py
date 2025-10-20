"""
LeetCode Problem 377: Combination Sum IV
Difficulty: Medium
Topics: Array, Dynamic Programming

Problem Description:
Given an array of distinct integers nums and a target integer target, return the number 
of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

Note that different sequences are counted as different combinations.

Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Example 2:
Input: nums = [9], target = 3
Output: 0

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 1000
- All the elements of nums are unique.
- 1 <= target <= 1000

Follow up: What if negative numbers are allowed in the given array? How does it change 
the problem? What limitation we need to add to the question to allow negative numbers?
"""

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        Initial solution with optimization using minimum value.
        
        Approach:
        - Use dynamic programming with bottom-up approach
        - dp[i] represents number of combinations that sum to i
        - Start from minimum value in nums to skip impossible targets
        - For each target value, try all numbers and sum up combinations
        
        Time Complexity: O(target * len(nums))
        Space Complexity: O(target)
        """
        combinations = [1] + [0] * target
        minimum = min(nums)

        for i in range(minimum, target + 1):
            for number in nums:
                if (i - number) >= 0 and combinations[i - number] > 0:
                    combinations[i] += combinations[i - number]

        return combinations[target]


class SolutionOptimal:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        Cleaner optimal solution.
        
        Approach:
        - Use dynamic programming with bottom-up approach
        - dp[i] represents number of combinations that sum to i
        - Base case: dp[0] = 1 (one way to make 0: use no numbers)
        - For each amount from 1 to target, try all numbers
        - If current amount >= number, add combinations from (amount - number)
        
        Time Complexity: O(target * len(nums))
        Space Complexity: O(target)
        
        Key Insight:
        - This is similar to coin change but counts permutations not combinations
        - Order matters: [1,2] and [2,1] are different
        - The outer loop iterates through targets (not nums) to count permutations
        """
        dp = [1] + [0] * target
        
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        
        return dp[target]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution_optimal = SolutionOptimal()
    
    # Test case 1
    nums1 = [1, 2, 3]
    target1 = 4
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output (Initial): {solution.combinationSum4(nums1, target1)}")
    print(f"Output (Optimal): {solution_optimal.combinationSum4(nums1, target1)}")
    print(f"Expected: 7\n")
    
    # Test case 2
    nums2 = [9]
    target2 = 3
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output (Initial): {solution.combinationSum4(nums2, target2)}")
    print(f"Output (Optimal): {solution_optimal.combinationSum4(nums2, target2)}")
    print(f"Expected: 0\n")
