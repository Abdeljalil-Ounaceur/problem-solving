"""
1018. Binary Prefix Divisible By 5
Difficulty: Easy
Topics: Array, Math, Bit Manipulation

You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray nums[0..i] 
(from most-significant-bit to least-significant-bit).

For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

Example 1:
Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.

Example 2:
Input: nums = [1,1,1]
Output: [false,false,false]

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
"""

from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        """
        Initial solution: Build the full number and check divisibility.
        
        Time Complexity: O(n) where n is the length of nums
        Space Complexity: O(n) for the result array
        
        Note: This solution works but can lead to very large numbers for long arrays.
        The curr value can grow exponentially, which may cause performance issues.
        """
        curr = 0
        res = [False] * len(nums)
        for i in range(len(nums)):
            curr = curr * 2 + nums[i]
            res[i] = curr % 5 == 0

        return res


class SolutionOptimal:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        """
        Optimal solution: Use modular arithmetic to keep numbers small.
        
        Key insight: We only care about divisibility by 5, not the actual value.
        By the properties of modular arithmetic: (a * b) % m = ((a % m) * b) % m
        So we can apply modulo 5 at each step to keep the number small.
        
        This prevents integer overflow and improves performance by keeping
        all intermediate values in the range [0, 4].
        
        Time Complexity: O(n) where n is the length of nums
        Space Complexity: O(n) for the result array
        """
        curr = 0
        res = [False] * len(nums)
        for i in range(len(nums)):
            curr = (curr * 2 + nums[i]) % 5
            res[i] = curr == 0

        return res
