"""
LeetCode Problem #76: Minimum Window Substring
Difficulty: Hard
Topics: Hash Table, String, Sliding Window

Problem Description:
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in 
the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?

Time Complexity: O(m + n) - optimal solution
Space Complexity: O(m + n) - for the hash maps
"""

from collections import defaultdict, Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Optimal solution using sliding window technique.
        
        The idea is to use two pointers (left and right) to maintain a sliding window.
        We expand the window by moving right pointer until we have a valid window
        (contains all characters from t), then we try to shrink it by moving left
        pointer while maintaining validity.
        """
        if not s or not t:
            return ""
        
        t_counter = Counter(t)
        required = len(t_counter)  # Number of unique characters in t
        
        left = 0
        right = 0
        formed = 0  # Number of unique chars in current window with desired frequency
        window_counts = defaultdict(int)
        
        best_len = float("inf")
        best_left = best_right = 0
        
        while right < len(s):
            # Add character from the right to the window
            char = s[right]
            window_counts[char] += 1
            
            # If the frequency of current character added equals the desired count
            # in t, increment the formed count by 1
            if char in t_counter and window_counts[char] == t_counter[char]:
                formed += 1
            
            # Try to contract the window until it ceases to be 'desirable'
            while left <= right and formed == required:
                # Save the smallest window until now
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left, best_right = left, right
                
                # The character at the left pointer is no longer part of the window
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in t_counter and window_counts[left_char] < t_counter[left_char]:
                    formed -= 1
                
                # Move the left pointer ahead for the next iteration
                left += 1
            
            # Keep expanding the window by moving right pointer
            right += 1
        
        return "" if best_len == float("inf") else s[best_left:best_right+1]


class SolutionUnoptimized:
    def minWindow(self, s: str, t: str) -> str:
        """
        Initial unoptimized solution.
        
        This solution has the right idea but is less efficient because it checks
        validity by iterating through all characters in t_counter for each position.
        """
        d = defaultdict(int)
        left = right = 0
        N = len(s)
        best_left = 0
        best_right = float("inf")
        t_counter = Counter(t)
        
        for right in range(N):
            valid = True
            left_most = s[left]
            right_most = s[right]
            d[right_most] += 1
            
            # Try to shrink window from left
            while((left_most not in t_counter or d[left_most] > t_counter[left_most]) and left < right):
                left += 1
                d[left_most] -= 1
                left_most = s[left]
            
            # Check if current window is valid (inefficient part)
            for c2 in t_counter:
                if d[c2] < t_counter[c2]:
                    valid = False
                    break
            
            if valid:
                if(right - left < best_right - best_left):
                    best_left, best_right = left, right
    
        return s[best_left:best_right+1] if best_right != float("inf") else ""


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution_unopt = SolutionUnoptimized()
    
    # Test case 1
    s1, t1 = "ADOBECODEBANC", "ABC"
    result1 = solution.minWindow(s1, t1)
    result1_unopt = solution_unopt.minWindow(s1, t1)
    print(f"Test 1: s='{s1}', t='{t1}'")
    print(f"Optimal: '{result1}' | Unoptimized: '{result1_unopt}'")
    print(f"Expected: 'BANC'\n")
    
    # Test case 2
    s2, t2 = "a", "a"
    result2 = solution.minWindow(s2, t2)
    result2_unopt = solution_unopt.minWindow(s2, t2)
    print(f"Test 2: s='{s2}', t='{t2}'")
    print(f"Optimal: '{result2}' | Unoptimized: '{result2_unopt}'")
    print(f"Expected: 'a'\n")
    
    # Test case 3
    s3, t3 = "a", "aa"
    result3 = solution.minWindow(s3, t3)
    result3_unopt = solution_unopt.minWindow(s3, t3)
    print(f"Test 3: s='{s3}', t='{t3}'")
    print(f"Optimal: '{result3}' | Unoptimized: '{result3_unopt}'")
    print(f"Expected: ''\n")
    
    # Additional test cases
    s4, t4 = "ADOBECODEBANC", "AABC"
    result4 = solution.minWindow(s4, t4)
    result4_unopt = solution_unopt.minWindow(s4, t4)
    print(f"Test 4: s='{s4}', t='{t4}'")
    print(f"Optimal: '{result4}' | Unoptimized: '{result4_unopt}'")
    print(f"Expected: 'ADOBEC'\n")
    
    # Edge case: empty strings
    s5, t5 = "", "a"
    result5 = solution.minWindow(s5, t5)
    result5_unopt = solution_unopt.minWindow(s5, t5)
    print(f"Test 5: s='{s5}', t='{t5}'")
    print(f"Optimal: '{result5}' | Unoptimized: '{result5_unopt}'")
    print(f"Expected: ''\n")
