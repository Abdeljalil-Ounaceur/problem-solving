"""
LeetCode Problem 121: Best Time to Buy and Sell Stock
Difficulty: Easy
Topics: Array, Dynamic Programming

Problem Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing 
a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Examples:
- Input: prices = [7,1,5,3,6,4], Output: 5
- Input: prices = [7,6,4,3,1], Output: 0

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Optimized one-pass solution using tracking minimum price and maximum profit.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - only using two variables
        
        Algorithm:
        1. Track the minimum price seen so far
        2. For each price, calculate profit if we sell at current price
        3. Update maximum profit if current profit is better
        
        Args:
            prices: List of stock prices for each day
            
        Returns:
            Maximum profit achievable, or 0 if no profit possible
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update minimum price if current price is lower
            min_price = min(min_price, price)
            # Calculate profit if we sell at current price and update max profit
            max_profit = max(max_profit, price - min_price)
            
        return max_profit


def test_solution():
    """Test cases for the Best Time to Buy and Sell Stock problem"""
    solution = Solution()
    
    # Test case 1: Example from problem
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = solution.maxProfit(prices1)
    print(f"Test 1 - Input: {prices1}")
    print(f"Expected: 5, Got: {result1}")
    assert result1 == 5, f"Test 1 failed: expected 5, got {result1}"
    
    # Test case 2: No profit possible
    prices2 = [7, 6, 4, 3, 1]
    result2 = solution.maxProfit(prices2)
    print(f"Test 2 - Input: {prices2}")
    print(f"Expected: 0, Got: {result2}")
    assert result2 == 0, f"Test 2 failed: expected 0, got {result2}"
    
    # Test case 3: Single element
    prices3 = [1]
    result3 = solution.maxProfit(prices3)
    print(f"Test 3 - Input: {prices3}")
    print(f"Expected: 0, Got: {result3}")
    assert result3 == 0, f"Test 3 failed: expected 0, got {result3}"
    
    # Test case 4: Two elements - profit possible
    prices4 = [1, 5]
    result4 = solution.maxProfit(prices4)
    print(f"Test 4 - Input: {prices4}")
    print(f"Expected: 4, Got: {result4}")
    assert result4 == 4, f"Test 4 failed: expected 4, got {result4}"
    
    # Test case 5: Two elements - no profit
    prices5 = [5, 1]
    result5 = solution.maxProfit(prices5)
    print(f"Test 5 - Input: {prices5}")
    print(f"Expected: 0, Got: {result5}")
    assert result5 == 0, f"Test 5 failed: expected 0, got {result5}"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
