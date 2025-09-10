"""
LeetCode Problem #3: Longest Substring Without Repeating Characters
Difficulty: Medium
Category: String, Hash Table, Sliding Window

Problem Description:
Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces

Test Cases:
1. "abcabcbb" -> 3
2. "bbbbb" -> 1
3. "pwwkew" -> 3
4. "" -> 0
5. " " -> 1

Contributors: u8tRAAB9Wu
"""

class Solution(object):
    def lengthOfLongestSubstring_initial(self, s):
        """
        Initial solution using sliding window with string slicing.
        
        Runtime: 18ms (Beats 80.47%)
        Memory: 12.57MB (Beats 85.69%)
        
        Args:
            s (str): Input string
            
        Returns:
            int: Length of longest substring without repeating characters
        """
        if len(s) < 0 or len(s) > 5*10**4:
            return -1
        
        sequence = s[0] if len(s) > 0 else ""
        start = 0
        end = 0
        
        while end < len(s):
            end += 1
            if (end >= len(s)):
                break
            if (s[end] not in s[start:end]):
                sequence = s[start:end+1] if len(sequence) < len(s[start:end+1]) else sequence
                continue
            else:
                while s[start] != s[end]:
                    start += 1
                start += 1

        return len(sequence)

    def lengthOfLongestSubstring_optimized(self, s):
        """
        Optimized solution using sliding window with hash set.
        
        Runtime: 25ms (Beats 49.49%)
        Memory: 13.35MB (Beats 16.61%)
        
        Args:
            s (str): Input string
            
        Returns:
            int: Length of longest substring without repeating characters
        """
        if len(s) > 5 * 10**4:
            return -1

        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

    def lengthOfLongestSubstring(self, s):
        """
        Main solution method (using optimized version).
        
        Args:
            s (str): Input string
            
        Returns:
            int: Length of longest substring without repeating characters
        """
        return self.lengthOfLongestSubstring_optimized(s)


# Test the solutions
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        "abcabcbb",  # Expected: 3
        "bbbbb",     # Expected: 1
        "pwwkew",    # Expected: 3
        "",          # Expected: 0
        " ",         # Expected: 1
        "dvdf",      # Expected: 3
        "anviaj"     # Expected: 5
    ]
    
    print("Testing Longest Substring Without Repeating Characters\n")
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Test {i}: '{test_case}'")
        
        # Test initial solution
        result_initial = solution.lengthOfLongestSubstring_initial(test_case)
        print(f"  Initial Solution: {result_initial}")
        
        # Test optimized solution
        result_optimized = solution.lengthOfLongestSubstring_optimized(test_case)
        print(f"  Optimized Solution: {result_optimized}")
        
        # Test main solution
        result_main = solution.lengthOfLongestSubstring(test_case)
        print(f"  Main Solution: {result_main}")
        print()
    
    print("All tests completed!")
