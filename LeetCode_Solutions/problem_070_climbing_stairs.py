"""
70. Climbing Stairs
Solved
Easy
Topics: Dynamic Programming, Math, Memoization
Companies: Adobe, Amazon, Apple, Google, Microsoft

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Optimal Solution: Dynamic Programming (Space Optimized)
        
        This is essentially a Fibonacci sequence problem where:
        - f(1) = 1 (one way to climb 1 step)
        - f(2) = 2 (two ways to climb 2 steps)
        - f(n) = f(n-1) + f(n-2) for n > 2
        
        The logic is: to reach step n, you can either:
        1. Come from step (n-1) and take 1 step
        2. Come from step (n-2) and take 2 steps
        
        Time Complexity: O(n) - single pass through n steps
        Space Complexity: O(1) - only using two variables
        
        Args:
            n: Number of steps to reach the top
            
        Returns:
            Number of distinct ways to climb to the top
        """
        prev2, prev1 = 0, 1
        for i in range(n):
            prev2, prev1 = prev1, prev2 + prev1
        return prev1

    def climbStairs_recursive_memoized(self, n: int) -> int:
        """
        Alternative Solution: Recursive with Memoization
        
        Time Complexity: O(n)
        Space Complexity: O(n) - for memoization and recursion stack
        """
        memo = {}
        
        def climb(steps):
            if steps in memo:
                return memo[steps]
            if steps <= 2:
                return steps
            
            memo[steps] = climb(steps - 1) + climb(steps - 2)
            return memo[steps]
        
        return climb(n)

    def climbStairs_dp_array(self, n: int) -> int:
        """
        Alternative Solution: Dynamic Programming with Array
        
        Time Complexity: O(n)
        Space Complexity: O(n) - for dp array
        """
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    n1 = 2
    result1 = solution.climbStairs(n1)
    print(f"Input: n = {n1}")
    print(f"Output: {result1}")
    print(f"Expected: 2")
    print()
    
    # Test case 2
    n2 = 3
    result2 = solution.climbStairs(n2)
    print(f"Input: n = {n2}")
    print(f"Output: {result2}")
    print(f"Expected: 3")
    print()
    
    # Test case 3 - edge case
    n3 = 1
    result3 = solution.climbStairs(n3)
    print(f"Input: n = {n3}")
    print(f"Output: {result3}")
    print(f"Expected: 1")
    print()
    
    # Test case 4 - larger input
    n4 = 5
    result4 = solution.climbStairs(n4)
    print(f"Input: n = {n4}")
    print(f"Output: {result4}")
    print(f"Expected: 8")
    print()
    
    # Verify all solutions give same result
    print("Verifying all solutions give same result:")
    for n in [1, 2, 3, 4, 5, 10]:
        opt = solution.climbStairs(n)
        rec = solution.climbStairs_recursive_memoized(n)
        arr = solution.climbStairs_dp_array(n)
        print(f"n={n}: Optimal={opt}, Recursive={rec}, Array={arr}, Match={opt==rec==arr}")
