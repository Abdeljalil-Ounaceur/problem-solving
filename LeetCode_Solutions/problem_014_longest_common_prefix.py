"""
LeetCode Problem #14: Longest Common Prefix
Difficulty: Easy
Topics: String, Trie

Problem:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

from typing import List

# ============================================================================
# Optimal Solution - Character-by-Character Comparison
# ============================================================================
class Solution:
    """
    Approach: Compare characters at each position across all strings
    Time Complexity: O(S) where S is the sum of all characters in all strings
    Space Complexity: O(1) - only using a few variables
    
    Key insight:
    - Start with the first string as the prefix
    - For each subsequent string, shrink the prefix by comparing character by character
    - Stop early if prefix becomes empty
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        
        for word in strs[1:]:
            i = 0
            while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
                i += 1
            prefix = prefix[:i]
            if not prefix:
                break
        
        return prefix


# ============================================================================
# Initial Solution - String Manipulation with Zip
# ============================================================================
class Solution_Initial:
    """
    Approach: Use zip to compare characters and string manipulation to find prefix
    Time Complexity: O(S) where S is the sum of all characters
    Space Complexity: O(m) where m is the length of the prefix (for string building)
    
    This approach is more creative but less efficient due to string operations.
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        for word in strs[1:]:
            prefix = ("".join(c1 if c1 == c2 else " " for c1, c2 in zip(prefix, word))).split(" ")[0]
        
        return prefix


# ============================================================================
# Alternative Solution - Vertical Scanning
# ============================================================================
class Solution_Vertical:
    """
    Approach: Compare characters column by column across all strings
    Time Complexity: O(S) where S is the sum of all characters
    Space Complexity: O(1)
    
    This approach scans vertically (character position by position) rather than
    horizontally (string by string).
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Iterate through character positions
        for i in range(len(strs[0])):
            char = strs[0][i]
            # Check if all strings have the same character at position i
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]
        
        # If we've gone through all characters of the first string
        return strs[0]


# ============================================================================
# Alternative Solution - Sorting
# ============================================================================
class Solution_Sorting:
    """
    Approach: Sort the array and compare only the first and last strings
    Time Complexity: O(n * m * log n) where n is number of strings, m is average length
    Space Complexity: O(1) if we don't count the sorting space
    
    Key insight:
    - After sorting, the first and last strings will be the most different
    - The common prefix of all strings is the common prefix of these two
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()
        first = strs[0]
        last = strs[-1]
        
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        return first[:i]


# ============================================================================
# Test Cases
# ============================================================================
if __name__ == "__main__":
    # Test with all solutions
    solutions = [
        ("Optimal (Character-by-Character)", Solution()),
        ("Initial (Zip with String Manipulation)", Solution_Initial()),
        ("Vertical Scanning", Solution_Vertical()),
        ("Sorting Approach", Solution_Sorting())
    ]
    
    test_cases = [
        (["flower", "flow", "flight"], "fl", "Common prefix 'fl'"),
        (["dog", "racecar", "car"], "", "No common prefix"),
        (["interspecies", "interstellar", "interstate"], "inters", "Longer common prefix"),
        (["throne", "throne"], "throne", "Identical strings"),
        (["", "b"], "", "Empty string in array"),
        (["a"], "a", "Single string"),
        (["ab", "a"], "a", "First string longer than second"),
        (["abc", "abcd", "ab"], "ab", "Varying lengths"),
        (["reflower", "flow", "flight"], "", "No common prefix with different first chars"),
        (["c", "acc", "ccc"], "", "No common prefix"),
        (["aa", "aa"], "aa", "Identical short strings"),
        (["", ""], "", "Two empty strings"),
    ]
    
    for name, solution in solutions:
        print(f"\n{'='*70}")
        print(f"Testing: {name}")
        print(f"{'='*70}")
        
        all_passed = True
        for strs, expected, description in test_cases:
            result = solution.longestCommonPrefix(strs)
            status = "✓" if result == expected else "✗"
            if result != expected:
                all_passed = False
            strs_str = str(strs)[:40] + "..." if len(str(strs)) > 40 else str(strs)
            print(f"{status} Input: {strs_str:43s} | Expected: '{expected:10s}' | Got: '{result:10s}' | {description}")
        
        print(f"\nResult: {'All tests passed! ✓' if all_passed else 'Some tests failed ✗'}")
