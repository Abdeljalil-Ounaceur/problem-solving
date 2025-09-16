"""
LeetCode Problem 5: Longest Palindromic Substring
Difficulty: Medium
Topics: String, Dynamic Programming

Problem Description:
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        if N <= 1:
           return s

        start, end = 0, 0

        for i in range(N-1):
            # Early termination optimization
            if(2*(N-i-1) + 1 < end-start):
                return s[start:end+1]

            # Check for both odd and even length palindromes
            for left, right in ((i, i), (i, i+1)):
                while(left >= 0 and right < N):
                    if(s[left] != s[right]):
                        break
                    else:
                        if(right - left > end - start):
                            start, end = left, right
                        left -= 1
                        right += 1
        
        return s[start:end+1]


# Test cases
def test_longest_palindrome():
    solution = Solution()
    
    # Test case 1
    assert solution.longestPalindrome("babad") in ["bab", "aba"]
    
    # Test case 2
    assert solution.longestPalindrome("cbbd") == "bb"
    
    # Additional test cases
    assert solution.longestPalindrome("a") == "a"
    assert solution.longestPalindrome("ac") == "a"
    assert solution.longestPalindrome("racecar") == "racecar"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindrome()
