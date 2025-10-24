"""
LeetCode Problem #91: Decode Ways
Difficulty: Medium
Topics: String, Dynamic Programming

Problem Description:
You have intercepted a secret message encoded as a string of numbers. The message is 
decoded via the following mapping:
"1" -> 'A', "2" -> 'B', ..., "25" -> 'Y', "26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you 
can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:
- "AAJF" with the grouping (1, 1, 10, 6)
- "KJF" with the grouping (11, 10, 6)
- The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).

Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. 
If the entire string cannot be decoded in any valid way, return 0.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

Constraints:
- 1 <= s.length <= 100
- s contains only digits and may contain leading zero(s).
"""

# ============================================================================
# Initial Solution (Complex State Tracking)
# ============================================================================
class Solution_Initial:
    """
    Initial solution with complex state tracking and multiple edge cases.
    
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(1) - only using a few variables
    
    This solution works but has overly complex conditional logic tracking
    previous decode states and couple decode states separately.
    """
    def numDecodings(self, s: str) -> int:
        prev_dec = prev_couple_dec = False
        count = 0
        prev2 = prev1 = 1

        for i in range(len(s)):
            dec = ( s[i] != "0" )   
            couple_dec = prev_dec and int(s[i-1:i+1]) in range(1,27)

            if dec and couple_dec:
                count = prev1+prev2
            elif couple_dec:
                if prev_couple_dec:
                    count = min(prev2,prev1)
            elif dec and i == 0:
                count=1
            elif not dec and i == len(s)-1:
                return 0
            elif not dec and not prev_dec:
                return 0
            elif not dec and not couple_dec:
                return 0

            prev_dec, prev_couple_dec = dec, couple_dec
            prev2, prev1 = prev1, count

        return prev1            


# ============================================================================
# Optimal Solution (Clean DP)
# ============================================================================
class Solution:
    """
    Optimal solution using clean dynamic programming approach.
    
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(1) - only using two variables for DP states
    
    Key Insights:
    1. Use DP where prev1 = ways to decode up to current position
    2. At each position, we can:
       - Decode single digit (if not '0'): add prev1 ways
       - Decode two digits (if valid 10-26): add prev2 ways
    3. Early exit for strings starting with '0'
    4. Similar to climbing stairs problem - sum of previous states
    
    Algorithm:
    1. Handle edge case: string starts with '0' → return 0
    2. Initialize prev2=1 (empty string), prev1=1 (first char if valid)
    3. For each position i from 1 to n-1:
       a. Check if single digit decode is valid (not '0')
       b. Check if two-digit decode is valid (10-26)
       c. Sum the ways from both possibilities
       d. Update prev2 and prev1 for next iteration
    4. Return prev1 (ways to decode entire string)
    
    Example walkthrough for s = "226":
    - Initial: prev2=1, prev1=1 (one way to decode "2")
    - i=1 (char '2'):
      * Single: '2' is valid → add prev1=1
      * Double: '22' is valid (10-26) → add prev2=1
      * count = 1+1 = 2, update prev2=1, prev1=2
    - i=2 (char '6'):
      * Single: '6' is valid → add prev1=2
      * Double: '26' is valid (10-26) → add prev2=1
      * count = 2+1 = 3, update prev2=2, prev1=3
    - Return 3
    """
    def numDecodings(self, s: str) -> int:
        # Early exit: string cannot start with '0'
        if not s or s[0]=="0":
            return 0

        # DP variables: prev2 = dp[i-2], prev1 = dp[i-1]
        # prev2=1 represents empty string (one way to decode nothing)
        # prev1=1 represents first character (already validated not '0')
        prev2 = prev1 = 1

        # Process each character starting from index 1
        for i in range(1,len(s)):
            # Check if current digit can be decoded alone (not '0')
            dec = ( s[i] != "0" )   
            
            # Check if last two digits form valid code (10-26)
            # Note: range(10,27) means 10 <= value <= 26
            couple_dec = int(s[i-1:i+1]) in range(10,27)

            # Calculate ways to decode up to current position
            count = 0
            if dec:
                # Can decode current digit alone: add ways from prev1
                count += prev1
            if couple_dec:
                # Can decode last two digits together: add ways from prev2
                count += prev2
 
            # Update DP states for next iteration
            prev2, prev1 = prev1, count

        return prev1


# ============================================================================
# Alternative Solution (Explicit DP Array)
# ============================================================================
class Solution_DP_Array:
    """
    Alternative solution using explicit DP array for clarity.
    
    Time Complexity: O(n)
    Space Complexity: O(n) - using DP array
    
    This is more intuitive but uses extra space. Good for understanding
    the DP recurrence relation before optimizing to O(1) space.
    """
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string
        dp[1] = 1  # First character (already validated)
        
        for i in range(2, n + 1):
            # Single digit decode
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            
            # Two digit decode
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]


# ============================================================================
# Test Cases
# ============================================================================
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Basic two-way decode
    assert solution.numDecodings("12") == 2  # "AB" or "L"
    
    # Test Case 2: Multiple decode paths
    assert solution.numDecodings("226") == 3  # "BZ", "VF", "BBF"
    
    # Test Case 3: Leading zero - invalid
    assert solution.numDecodings("06") == 0
    
    # Test Case 4: Single digit
    assert solution.numDecodings("1") == 1
    
    # Test Case 5: Zero in middle - must be part of 10 or 20
    assert solution.numDecodings("10") == 1  # Only "J"
    assert solution.numDecodings("27") == 1  # Only "BG" (27 > 26)
    
    # Test Case 6: Multiple zeros
    assert solution.numDecodings("100") == 0  # "10" + "0" invalid
    
    # Test Case 7: Long valid string
    assert solution.numDecodings("111111") == 13
    
    print("All test cases passed!")
