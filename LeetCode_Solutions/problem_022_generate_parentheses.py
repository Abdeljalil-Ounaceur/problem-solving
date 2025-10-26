"""
LeetCode Problem 22: Generate Parentheses
Difficulty: Medium
Topics: String, Dynamic Programming, Backtracking

Problem Description:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
- 1 <= n <= 8

Time Complexity: O(4^n / sqrt(n)) - Catalan number growth
Space Complexity: O(4^n / sqrt(n)) - for storing results
"""

from typing import List
from collections import defaultdict


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Initial Solution: Dynamic Programming with Catalan Number Pattern
        
        Approach:
        - Use DP where res[i] contains all valid combinations with i pairs
        - For each i, generate combinations by:
          1. Taking j pairs from previous results (res[j])
          2. Wrapping them with one pair: f"({item})"
          3. Concatenating with remaining pairs: res[i-j-1]
        - This follows the Catalan number recurrence relation
        
        Time Complexity: O(4^n / sqrt(n)) - Catalan number
        Space Complexity: O(4^n / sqrt(n)) - for storing all valid combinations
        
        Example walkthrough for n=2:
        - res[0] = {""}
        - res[1]: j=0 -> f"({''}){''}' = "()"
        - res[2]: 
          - j=0 -> f"({''}){'()'}" = "()()"
          - j=1 -> f"({'()'}){''}' = "(())"
        """
        res = defaultdict(set)
        res[0].add("")

        for i in range(n + 1):
            for j in range(i):
                for item in res[j]:
                    res[i].update([f"({item}){compl}" for compl in res[i - j - 1]])
        
        return list(res[n])


class OptimalSolution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Optimal Solution: Backtracking (Super Elegant)
        
        Approach:
        - Build valid combinations character by character using backtracking
        - Track count of open '(' and close ')' parentheses
        - Rules for validity:
          1. Can add '(' if open_count < n
          2. Can add ')' if close_count < open_count (ensures proper closing)
        - When length reaches 2*n, we have a complete valid combination
        
        Time Complexity: O(4^n / sqrt(n)) - same as DP but with better constants
        Space Complexity: O(n) - recursion depth, plus O(4^n / sqrt(n)) for results
        
        Key Insight:
        - This approach is more intuitive than DP
        - Directly builds valid strings by ensuring closing parens never exceed opening
        - Avoids generating invalid combinations entirely
        
        Example walkthrough for n=2:
        - Start: current="", open=0, close=0
        - Add '(': current="(", open=1, close=0
          - Add '(': current="((", open=2, close=0
            - Add ')': current="(()", open=2, close=1
              - Add ')': current="(())", open=2, close=2 → COMPLETE
          - Add ')': current="()", open=1, close=1
            - Add '(': current="()(", open=2, close=1
              - Add ')': current="()()", open=2, close=2 → COMPLETE
        """
        res = []

        def backtrack(current, open_count, close_count):
            # Base case: complete valid combination
            if len(current) == 2 * n:
                res.append(current)
                return

            # Add opening parenthesis if we haven't used all n pairs
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add closing parenthesis if it doesn't exceed opening count
            # This ensures we never have more closing than opening at any point
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res


# Test cases
def test_solutions():
    """Test both solutions with the provided examples"""
    solution = Solution()
    optimal = OptimalSolution()
    
    # Test case 1: n = 3
    n1 = 3
    result1 = sorted(solution.generateParenthesis(n1))
    result1_optimal = sorted(optimal.generateParenthesis(n1))
    expected1 = sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
    
    print(f"Test 1 (n={n1}):")
    print(f"Initial Solution: {result1}")
    print(f"Optimal Solution: {result1_optimal}")
    print(f"Expected: {expected1}")
    print(f"Initial Match: {result1 == expected1}")
    print(f"Optimal Match: {result1_optimal == expected1}")
    print()
    
    # Test case 2: n = 1
    n2 = 1
    result2 = sorted(solution.generateParenthesis(n2))
    result2_optimal = sorted(optimal.generateParenthesis(n2))
    expected2 = ["()"]
    
    print(f"Test 2 (n={n2}):")
    print(f"Initial Solution: {result2}")
    print(f"Optimal Solution: {result2_optimal}")
    print(f"Expected: {expected2}")
    print(f"Initial Match: {result2 == expected2}")
    print(f"Optimal Match: {result2_optimal == expected2}")
    print()
    
    # Additional test case: n = 2
    n3 = 2
    result3 = sorted(solution.generateParenthesis(n3))
    result3_optimal = sorted(optimal.generateParenthesis(n3))
    expected3 = sorted(["(())", "()()"])
    
    print(f"Test 3 (n={n3}):")
    print(f"Initial Solution: {result3}")
    print(f"Optimal Solution: {result3_optimal}")
    print(f"Expected: {expected3}")
    print(f"Initial Match: {result3 == expected3}")
    print(f"Optimal Match: {result3_optimal == expected3}")
    print()
    
    # Edge case: n = 4
    n4 = 4
    result4 = solution.generateParenthesis(n4)
    result4_optimal = optimal.generateParenthesis(n4)
    
    print(f"Test 4 (n={n4}):")
    print(f"Initial Solution count: {len(result4)}")
    print(f"Optimal Solution count: {len(result4_optimal)}")
    print(f"Counts match: {len(result4) == len(result4_optimal)}")
    print(f"Sets match: {set(result4) == set(result4_optimal)}")
    
    # The 4th Catalan number is 14
    print(f"Expected count (4th Catalan number): 14")


if __name__ == "__main__":
    test_solutions()