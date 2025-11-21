"""
LeetCode Problem #9: Palindrome Number
Difficulty: Easy
Topics: Math

Problem:
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-2^31 <= x <= 2^31 - 1

Follow up: Could you solve it without converting the integer to a string?
"""

# ============================================================================
# Initial Solution - Two Pointer Approach with String Conversion
# ============================================================================
class Solution_Initial:
    """
    Approach: Convert to string and use two pointers from center
    Time Complexity: O(n) where n is number of digits
    Space Complexity: O(n) for string conversion
    """
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left = (len(x)-1)//2
        right = len(x)//2
        while (left >= 0):
            if x[left] != x[right]:
                return False
            left -= 1
            right +=1
        return True


# ============================================================================
# Optimal Solution - String Reversal
# ============================================================================
class Solution:
    """
    Approach: Convert to string and compare with reversed string
    Time Complexity: O(n) where n is number of digits
    Space Complexity: O(n) for string conversion
    
    This is the cleanest and most Pythonic solution when string conversion is allowed.
    """
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]


# ============================================================================
# Alternative Solution - Without String Conversion (Follow-up)
# ============================================================================
class Solution_NoString:
    """
    Approach: Reverse half of the number mathematically
    Time Complexity: O(log n) where n is the value of x (number of digits)
    Space Complexity: O(1)
    
    Key insights:
    1. Negative numbers are never palindromes
    2. Numbers ending in 0 are not palindromes (except 0 itself)
    3. Only need to reverse half the number and compare
    """
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (except 0) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        # Reverse the second half of the number
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # For even length: x == reversed_half
        # For odd length: x == reversed_half // 10 (middle digit doesn't matter)
        return x == reversed_half or x == reversed_half // 10


# ============================================================================
# Test Cases
# ============================================================================
if __name__ == "__main__":
    # Test with all three solutions
    solutions = [
        ("Initial (Two Pointer)", Solution_Initial()),
        ("Optimal (String Reversal)", Solution()),
        ("No String Conversion", Solution_NoString())
    ]
    
    test_cases = [
        (121, True, "121 reads the same forwards and backwards"),
        (-121, False, "Negative numbers are not palindromes"),
        (10, False, "10 reads as 01 backwards"),
        (0, True, "0 is a palindrome"),
        (12321, True, "Odd length palindrome"),
        (1221, True, "Even length palindrome"),
        (123, False, "Not a palindrome"),
        (1, True, "Single digit is palindrome"),
    ]
    
    for name, solution in solutions:
        print(f"\n{'='*60}")
        print(f"Testing: {name}")
        print(f"{'='*60}")
        
        all_passed = True
        for x, expected, description in test_cases:
            result = solution.isPalindrome(x)
            status = "✓" if result == expected else "✗"
            if result != expected:
                all_passed = False
            print(f"{status} Input: {x:6d} | Expected: {str(expected):5s} | Got: {str(result):5s} | {description}")
        
        print(f"\nResult: {'All tests passed! ✓' if all_passed else 'Some tests failed ✗'}")
