"""
LeetCode Problem 150: Evaluate Reverse Polish Notation
Difficulty: Medium
Topics: Array, Math, Stack

Problem Description:
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Optimal Solution: Stack-based evaluation
        
        Approach:
        - Use a stack to store operands
        - When encountering a number, push it onto the stack
        - When encountering an operator, pop two operands, apply the operation, and push result back
        - The order matters: second popped value is the first operand (num1), first popped is second operand (num2)
        - For division, use int(num1/num2) to truncate toward zero (handles negative division correctly)
        
        Time Complexity: O(n) where n is the number of tokens - single pass through all tokens
        Space Complexity: O(n) for the stack in worst case (all numbers before any operators)
        
        Key Insights:
        - RPN evaluation naturally maps to stack operations
        - Pop order is important: second pop is left operand, first pop is right operand
        - int(a/b) truncates toward zero for both positive and negative results
        """
        stack = []
        ops = ("+", "-", "*", "/")
        
        for token in tokens:
            if token in ops:
                # Pop in reverse order: num2 first, then num1
                num2, num1 = stack.pop(), stack.pop()
                
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    # int() truncates toward zero (correct for negative division)
                    stack.append(int(num1 / num2))
            else:
                # It's a number, push to stack
                stack.append(int(token))
        
        return stack.pop()


# Alternative Solution: Using operator dictionary
class SolutionAlternative:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Alternative approach using operator dictionary with lambda functions
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        
        # Define operations using lambda functions
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        
        for token in tokens:
            if token in operations:
                num2, num1 = stack.pop(), stack.pop()
                stack.append(operations[token](num1, num2))
            else:
                stack.append(int(token))
        
        return stack.pop()


"""
Test Cases:
"""
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    tokens1 = ["2", "1", "+", "3", "*"]
    assert solution.evalRPN(tokens1) == 9, "Test Case 1 Failed"
    print(f"Test Case 1 Passed: {tokens1} = 9")
    
    # Test Case 2
    tokens2 = ["4", "13", "5", "/", "+"]
    assert solution.evalRPN(tokens2) == 6, "Test Case 2 Failed"
    print(f"Test Case 2 Passed: {tokens2} = 6")
    
    # Test Case 3
    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    assert solution.evalRPN(tokens3) == 22, "Test Case 3 Failed"
    print(f"Test Case 3 Passed: {tokens3} = 22")
    
    # Test Case 4: Single number
    tokens4 = ["42"]
    assert solution.evalRPN(tokens4) == 42, "Test Case 4 Failed"
    print(f"Test Case 4 Passed: {tokens4} = 42")
    
    # Test Case 5: Negative division
    tokens5 = ["4", "-2", "/"]
    assert solution.evalRPN(tokens5) == -2, "Test Case 5 Failed"
    print(f"Test Case 5 Passed: {tokens5} = -2")
    
    print("\nAll test cases passed!")
