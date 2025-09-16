"""
LeetCode Problem 647: Palindromic Substrings
Difficulty: Medium
Topics: String, Dynamic Programming

Problem Description:
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        # Use expand around centers approach to count all palindromic substrings
        n_of_palindromes = 0
        N = len(s)
        
        for i in range(N):
            # Check for both odd and even length palindromes centered at i
            for left, right in ((i, i), (i, i+1)):
                while (left >= 0 and right < N):
                    if(s[left] == s[right]):
                        n_of_palindromes += 1
                    else:
                        break
                    left -= 1
                    right += 1
        
        return n_of_palindromes


# Test cases
def test_count_substrings():
    solution = Solution()
    
    # Test case 1
    assert solution.countSubstrings("abc") == 3
    
    # Test case 2
    assert solution.countSubstrings("aaa") == 6
    
    # Additional test cases
    assert solution.countSubstrings("a") == 1
    assert solution.countSubstrings("aa") == 3  # "a", "a", "aa"
    assert solution.countSubstrings("racecar") == 10  # "r", "a", "c", "e", "c", "a", "r", "cec", "aceca", "racecar"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_count_substrings()
