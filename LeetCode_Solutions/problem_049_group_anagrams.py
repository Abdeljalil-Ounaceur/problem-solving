"""
49. Group Anagrams
Solved
Medium
Topics
Companies

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Optimized solution using sorted characters as key (beats 99% of users).
        
        Time Complexity: O(n * m * log m) where n is number of strings, m is average string length
        Space Complexity: O(n * m) for storing the groups
        """
        d = defaultdict(list)
        for s in strs:
            cs = tuple(sorted(s))
            d[cs].append(s)
        
        return list(d.values())


class SolutionCharacterCount:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Alternative solution using character frequency counting (allegedly optimal but only beats 40%).
        
        Time Complexity: O(n * m) where n is number of strings, m is average string length
        Space Complexity: O(n * m) for storing the groups
        
        Note: Despite better theoretical time complexity, this approach may be slower in practice
        due to the overhead of creating and hashing 26-element tuples for each string.
        """
        d = defaultdict(list)
        for s in strs:
            cs = [0] * 26
            for ch in s:
                cs[ord(ch) - ord("a")] += 1
            cs = tuple(cs)
            
            d[cs].append(s)
        
        return list(d.values())


def test_solution():
    """Test cases for the solution"""
    sol = Solution()
    sol_count = SolutionCharacterCount()
    
    # Test case 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected1 = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    result1 = sol.groupAnagrams(strs1)
    result1_count = sol_count.groupAnagrams(strs1)
    
    # Sort for comparison since order doesn't matter
    result1_sorted = [sorted(group) for group in sorted(result1)]
    result1_count_sorted = [sorted(group) for group in sorted(result1_count)]
    expected1_sorted = [sorted(group) for group in sorted(expected1)]
    
    print(f"Test 1: strs = {strs1}")
    print(f"Expected: {expected1_sorted}")
    print(f"Got (sorted): {result1_sorted}")
    print(f"Got (char count): {result1_count_sorted}")
    assert result1_sorted == expected1_sorted and result1_count_sorted == expected1_sorted
    
    # Test case 2
    strs2 = [""]
    expected2 = [[""]]
    result2 = sol.groupAnagrams(strs2)
    result2_count = sol_count.groupAnagrams(strs2)
    print(f"Test 2: strs = {strs2}")
    print(f"Expected: {expected2}, Got: {result2} (sorted), {result2_count} (char count)")
    assert result2 == expected2 and result2_count == expected2
    
    # Test case 3
    strs3 = ["a"]
    expected3 = [["a"]]
    result3 = sol.groupAnagrams(strs3)
    result3_count = sol_count.groupAnagrams(strs3)
    print(f"Test 3: strs = {strs3}")
    print(f"Expected: {expected3}, Got: {result3} (sorted), {result3_count} (char count)")
    assert result3 == expected3 and result3_count == expected3
    
    # Test case 4 - edge case with duplicates
    strs4 = ["abc", "bca", "cab", "xyz", "zyx", "yxz"]
    result4 = sol.groupAnagrams(strs4)
    result4_count = sol_count.groupAnagrams(strs4)
    print(f"Test 4: strs = {strs4}")
    print(f"Got (sorted): {[sorted(group) for group in sorted(result4)]}")
    print(f"Got (char count): {[sorted(group) for group in sorted(result4_count)]}")
    
    # Verify we have 2 groups of 3 anagrams each
    assert len(result4) == 2 and all(len(group) == 3 for group in result4)
    assert len(result4_count) == 2 and all(len(group) == 3 for group in result4_count)
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
