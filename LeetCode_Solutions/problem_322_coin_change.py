"""
LeetCode Problem #322: Coin Change
Difficulty: Medium
Topics: Array, Dynamic Programming, Breadth-First Search

Problem Description:
You are given an integer array coins representing coins of different denominations and an integer 
amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
"""

from typing import List


class InitialSolution:
    """
    Initial solution using dynamic programming with bottom-up approach.
    
    Time Complexity: O(amount * len(coins))
    - We iterate through all amounts from 1 to amount
    - For each amount, we check all coins
    
    Space Complexity: O(amount)
    - We use a DP array of size amount + 1
    
    Approach:
    - Create a DP array where dp[i] represents the minimum number of coins needed to make amount i
    - Initialize all values to infinity except dp[0] = 0 (base case: 0 coins needed for amount 0)
    - For each amount from 1 to target amount:
      - Try using each coin denomination
      - If coin value <= current amount, update dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    - Return dp[amount] if it's not infinity, otherwise return -1
    """
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        amounts = [float("inf")] * (amount + 1)
        amounts[0] = 0

        for i in range(1, amount + 1):
            min_value = float("inf")
            for j in range(len(coins)):
                if coins[j] <= i:
                    min_value = min(min_value, amounts[i - coins[j]])
            amounts[i] = 1 + min_value
        
        if amounts[amount] != float("inf"):
            return amounts[amount]
        
        return -1


class OptimalSolution:
    """
    Cleaner dynamic programming solution with improved readability.
    
    Time Complexity: O(amount * len(coins))
    - Same as initial solution
    
    Space Complexity: O(amount)
    - Same as initial solution
    
    Improvements over initial solution:
    - More Pythonic variable naming (dp instead of amounts)
    - Cleaner loop structure (iterating over coins directly instead of indices)
    - Additional check for dp[a - c] != float("inf") to avoid unnecessary operations
    - More concise final return statement
    """
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if c <= a and dp[a - c] != float("inf"):
                    dp[a] = min(dp[a], dp[a - c] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1


# Test cases
if __name__ == "__main__":
    solution = OptimalSolution()
    
    # Test case 1
    coins1 = [1, 2, 5]
    amount1 = 11
    print(f"Input: coins = {coins1}, amount = {amount1}")
    print(f"Output: {solution.coinChange(coins1, amount1)}")  # Expected: 3
    print()
    
    # Test case 2
    coins2 = [2]
    amount2 = 3
    print(f"Input: coins = {coins2}, amount = {amount2}")
    print(f"Output: {solution.coinChange(coins2, amount2)}")  # Expected: -1
    print()
    
    # Test case 3
    coins3 = [1]
    amount3 = 0
    print(f"Input: coins = {coins3}, amount = {amount3}")
    print(f"Output: {solution.coinChange(coins3, amount3)}")  # Expected: 0
