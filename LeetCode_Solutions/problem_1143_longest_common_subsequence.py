"""
LeetCode Problem #1143: Longest Common Subsequence
Difficulty: Medium
Topics: String, Dynamic Programming
Date: 2025-10-17

Problem Description:
Given two strings text1 and text2, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some 
characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.
"""


class Solution:
    """
    Optimal Solution: 2D Dynamic Programming
    
    Approach:
    - Create a 2D DP table where dp[i][j] represents the length of LCS 
      between text1[0:i] and text2[0:j]
    - If characters match: dp[i][j] = dp[i-1][j-1] + 1
    - If characters don't match: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    - The answer is in dp[m][n]
    
    Time Complexity: O(m * n) where m = len(text1), n = len(text2)
    Space Complexity: O(m * n) for the DP table
    
    Note: Failed to solve this problem within the time limit. This is the optimal solution.
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    text1 = "abcde"
    text2 = "ace"
    print(f"Input: text1 = '{text1}', text2 = '{text2}'")
    print(f"Output: {solution.longestCommonSubsequence(text1, text2)}")
    print(f"Expected: 3\n")
    
    # Test case 2
    text1 = "abc"
    text2 = "abc"
    print(f"Input: text1 = '{text1}', text2 = '{text2}'")
    print(f"Output: {solution.longestCommonSubsequence(text1, text2)}")
    print(f"Expected: 3\n")
    
    # Test case 3
    text1 = "abc"
    text2 = "def"
    print(f"Input: text1 = '{text1}', text2 = '{text2}'")
    print(f"Output: {solution.longestCommonSubsequence(text1, text2)}")
    print(f"Expected: 0\n")
