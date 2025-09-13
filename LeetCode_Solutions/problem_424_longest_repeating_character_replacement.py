"""
424. Longest Repeating Character Replacement
Solved
Medium
Topics
Companies

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Unoptimized solution: For each character position, expand left and right
        while tracking how many replacements are needed.
        
        Time Complexity: O(n^2)
        Space Complexity: O(k)
        """
        N = len(s)
        max_length = 0
        
        for i in range(N):
            c = s[i]
            r = i+1
            l = i-1
            right_k = left_k = 0
            k_to_length_right = [0]*(k+1)
            k_to_length_left = [0]*(k+1)
            left_done = right_done = False
            
            while ((not (left_done and right_done)) and (r < N or l >= 0)):
                if(r < N and not right_done):
                    if (s[r] == s[i]):
                        k_to_length_right[right_k] += 1
                    elif(right_k < k):
                        right_k += 1
                        k_to_length_right[right_k] = k_to_length_right[right_k-1] + 1
                    else:
                        right_done = True
                    r += 1
                else:
                    while(right_k < k):
                        right_k += 1
                        k_to_length_right[right_k] = k_to_length_right[right_k-1]
                    right_done = True
                    
                if(l >= 0 and not left_done):
                    if (s[l] == s[i]):
                        k_to_length_left[left_k] += 1
                    elif(left_k < k):
                        left_k += 1
                        k_to_length_left[left_k] = k_to_length_left[left_k-1] + 1
                    else:
                        left_done = True
                    l -= 1
                else:
                    while(left_k < k):
                        left_k += 1
                        k_to_length_left[left_k] = k_to_length_left[left_k-1]
                    left_done = True
                
            k_to_length_left = list(reversed(k_to_length_left))
            max_current = max([1 + k_to_length_left[i] + k_to_length_right[i] for i in range(k+1)])
            max_length = max(max_length, max_current)
        
        return max_length


class SolutionOptimized:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Optimized sliding window solution using character frequency counting.
        
        Time Complexity: O(n)
        Space Complexity: O(1) - at most 26 characters
        """
        from collections import defaultdict
        
        left = 0
        max_length = 0
        max_freq = 0
        char_count = defaultdict(int)
        
        for right in range(len(s)):
            char_count[s[right]] += 1
            max_freq = max(max_freq, char_count[s[right]])
            
            # If window size - max_freq > k, we need to shrink the window
            if (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length


def test_solution():
    """Test cases for the solution"""
    sol = Solution()
    sol_opt = SolutionOptimized()
    
    # Test case 1
    s1, k1 = "ABAB", 2
    expected1 = 4
    result1 = sol.characterReplacement(s1, k1)
    result1_opt = sol_opt.characterReplacement(s1, k1)
    print(f"Test 1: s='{s1}', k={k1}")
    print(f"Expected: {expected1}, Got: {result1} (unoptimized), {result1_opt} (optimized)")
    assert result1 == expected1 and result1_opt == expected1
    
    # Test case 2
    s2, k2 = "AABABBA", 1
    expected2 = 4
    result2 = sol.characterReplacement(s2, k2)
    result2_opt = sol_opt.characterReplacement(s2, k2)
    print(f"Test 2: s='{s2}', k={k2}")
    print(f"Expected: {expected2}, Got: {result2} (unoptimized), {result2_opt} (optimized)")
    assert result2 == expected2 and result2_opt == expected2
    
    # Test case 3 - edge case
    s3, k3 = "AAAA", 0
    expected3 = 4
    result3 = sol.characterReplacement(s3, k3)
    result3_opt = sol_opt.characterReplacement(s3, k3)
    print(f"Test 3: s='{s3}', k={k3}")
    print(f"Expected: {expected3}, Got: {result3} (unoptimized), {result3_opt} (optimized)")
    assert result3 == expected3 and result3_opt == expected3
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
