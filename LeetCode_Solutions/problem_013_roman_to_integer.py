"""
LeetCode Problem #13: Roman to Integer
Difficulty: Easy
Topics: Hash Table, Math, String

Problem:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

# ============================================================================
# Optimal Solution - Single Pass with Lookahead
# ============================================================================
class Solution:
    """
    Approach: Iterate through the string and compare each symbol with the next one
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(1) - only using a fixed-size dictionary
    
    Key insight:
    - If current symbol value < next symbol value, subtract current value
    - Otherwise, add current value
    - Always add the last symbol
    """
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        for i in range(len(s) - 1):
            total += d[s[i]] if d[s[i+1]] <= d[s[i]] else -d[s[i]]
        total += d[s[-1]]

        return total


# ============================================================================
# Alternative Solution - Explicit Subtraction Cases
# ============================================================================
class Solution_Explicit:
    """
    Approach: Handle all subtraction cases explicitly
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(1)
    
    This approach is more verbose but makes the logic clearer for beginners.
    """
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        # Handle special subtraction cases
        special_cases = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        
        total = 0
        i = 0
        
        while i < len(s):
            # Check if current and next character form a special case
            if i + 1 < len(s) and s[i:i+2] in special_cases:
                total += special_cases[s[i:i+2]]
                i += 2
            else:
                total += values[s[i]]
                i += 1
        
        return total


# ============================================================================
# Test Cases
# ============================================================================
if __name__ == "__main__":
    # Test with both solutions
    solutions = [
        ("Optimal (Lookahead)", Solution()),
        ("Explicit Subtraction Cases", Solution_Explicit())
    ]
    
    test_cases = [
        ("III", 3, "Simple addition: I + I + I"),
        ("LVIII", 58, "L + V + I + I + I = 50 + 5 + 3"),
        ("MCMXCIV", 1994, "M + CM + XC + IV = 1000 + 900 + 90 + 4"),
        ("IV", 4, "Subtraction case: 5 - 1"),
        ("IX", 9, "Subtraction case: 10 - 1"),
        ("XL", 40, "Subtraction case: 50 - 10"),
        ("XC", 90, "Subtraction case: 100 - 10"),
        ("CD", 400, "Subtraction case: 500 - 100"),
        ("CM", 900, "Subtraction case: 1000 - 100"),
        ("MMMCMXCIX", 3999, "Maximum value: 3000 + 900 + 90 + 9"),
        ("I", 1, "Single character"),
        ("M", 1000, "Single character (largest)"),
        ("MCMLIV", 1954, "M + CM + L + IV = 1000 + 900 + 50 + 4"),
    ]
    
    for name, solution in solutions:
        print(f"\n{'='*70}")
        print(f"Testing: {name}")
        print(f"{'='*70}")
        
        all_passed = True
        for s, expected, description in test_cases:
            result = solution.romanToInt(s)
            status = "✓" if result == expected else "✗"
            if result != expected:
                all_passed = False
            print(f"{status} Input: {s:12s} | Expected: {expected:4d} | Got: {result:4d} | {description}")
        
        print(f"\nResult: {'All tests passed! ✓' if all_passed else 'Some tests failed ✗'}")
