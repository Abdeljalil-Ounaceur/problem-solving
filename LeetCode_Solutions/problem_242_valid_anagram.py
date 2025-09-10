"""
LeetCode Problem #242: Valid Anagram
Difficulty: Easy
Topics: Hash Table, String, Sorting

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        d = dict()

        if len_s != len_t:
            return False

        for c1, c2 in zip(s, t):
            d[c1] = d.get(c1, 0) + 1
            d[c2] = d.get(c2, 0) - 1
        
        return all(val == 0 for val in d.values())

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1, t1 = "anagram", "nagaram"
    print(f"Test 1: s='{s1}', t='{t1}' -> {solution.isAnagram(s1, t1)}")  # Expected: True
    
    # Test case 2
    s2, t2 = "rat", "car"
    print(f"Test 2: s='{s2}', t='{t2}' -> {solution.isAnagram(s2, t2)}")  # Expected: False
