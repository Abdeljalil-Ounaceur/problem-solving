"""
LeetCode Problem #20: Valid Parentheses
Difficulty: Easy
Topics: String, Stack

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        twins = {")":"(", "]":"[", "}":"{"}
        stack = []
        
        for c in s:
            if c in "([{":
                stack.append(c)
            elif stack and stack[-1] == twins[c]:
                stack.pop()
            else:
                return False
        
        return not stack

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1 = "()"
    print(f"Test 1: s='{s1}' -> {solution.isValid(s1)}")  # Expected: True
    
    # Test case 2
    s2 = "()[]{}"
    print(f"Test 2: s='{s2}' -> {solution.isValid(s2)}")  # Expected: True
    
    # Test case 3
    s3 = "(]"
    print(f"Test 3: s='{s3}' -> {solution.isValid(s3)}")  # Expected: False
    
    # Test case 4
    s4 = "([])"
    print(f"Test 4: s='{s4}' -> {solution.isValid(s4)}")  # Expected: True
    
    # Test case 5
    s5 = "([)]"
    print(f"Test 5: s='{s5}' -> {solution.isValid(s5)}")  # Expected: False

