"""
LeetCode Problem #300: Longest Increasing Subsequence
Difficulty: Medium
Topics: Array, Binary Search, Dynamic Programming

Problem:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4
"""

from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Optimal Solution: Binary Search with Patience Sorting
        
        Time Complexity: O(n log n) - iterate through array once, binary search for each element
        Space Complexity: O(n) - lis array can grow up to size n
        
        Algorithm:
        - Maintain a list 'lis' that represents the smallest tail element for all increasing 
          subsequences of length i+1 in lis[i]
        - For each number, use binary search to find its position in lis
        - If position equals length of lis, append (found a longer subsequence)
        - Otherwise, replace element at position (found a better tail for that length)
        
        Key Insight: This is the "Patience Sorting" algorithm. The lis array doesn't 
        necessarily contain an actual LIS, but its length equals the LIS length.
        """
        lis = []
        
        for num in nums:
            pos = bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num
        
        return len(lis)


class SolutionInitial:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Initial Solution: Using SortedDict (third-party library)
        
        Time Complexity: O(n^2 log n) - for each element, iterate through sorted dict
        Space Complexity: O(n) - dictionary stores at most n elements
        
        Note: This solution works but requires the sortedcontainers library.
        The optimal solution above is preferred as it uses only standard library.
        """
        from sortedcontainers import SortedDict
        
        d = SortedDict()

        for i in range(len(nums)):
            maximum = 0
            for num in d:
                if num >= nums[i]:
                    break
                maximum = max(maximum, d[num])
        
            d[nums[i]] = maximum + 1
    
        return max(d.values())


class SolutionDP:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Alternative Solution: Dynamic Programming
        
        Time Complexity: O(n^2) - nested loops through array
        Space Complexity: O(n) - dp array
        
        Algorithm:
        - dp[i] represents the length of LIS ending at index i
        - For each position i, check all previous positions j < i
        - If nums[j] < nums[i], we can extend the LIS ending at j
        - dp[i] = max(dp[j] + 1) for all valid j
        """
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n  # Each element is at least a subsequence of length 1
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
