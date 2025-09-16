"""
LeetCode Problem #11: Container With Most Water
Difficulty: Medium
Topics: Array, Two Pointers, Greedy

Problem Description:
You are given an integer array height of length n. There are n vertical lines drawn such that 
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains 
the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Solution Approach:
Two Pointers technique - Start with the widest container (leftmost and rightmost lines) and 
move the pointer with the smaller height inward. This is optimal because moving the pointer 
with the larger height would only decrease the area since the width decreases and the height 
is limited by the smaller line.

Time Complexity: O(n) - Single pass through the array
Space Complexity: O(1) - Only using constant extra space
"""

class Solution:
    def maxArea(self, height):
        """
        Find the maximum area of water that can be contained between two lines.
        
        Args:
            height: List[int] - Array of heights representing vertical lines
            
        Returns:
            int - Maximum area of water that can be contained
        """
        N = len(height)
        start = 0
        end = N - 1
        max_area = (end - start) * (min(height[end], height[start]))

        while start < end:
            area = (end - start) * min(height[end], height[start])
            max_area = max(max_area, area)
            
            # Move the pointer with smaller height inward
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area


# Test cases
def test_solution():
    """Test the solution with provided examples"""
    solution = Solution()
    
    # Test case 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result1 = solution.maxArea(height1)
    print(f"Test 1: height = {height1}")
    print(f"Expected: 49, Got: {result1}")
    assert result1 == 49, f"Test 1 failed: expected 49, got {result1}"
    
    # Test case 2
    height2 = [1, 1]
    result2 = solution.maxArea(height2)
    print(f"Test 2: height = {height2}")
    print(f"Expected: 1, Got: {result2}")
    assert result2 == 1, f"Test 2 failed: expected 1, got {result2}"
    
    # Additional test case
    height3 = [1, 2, 1]
    result3 = solution.maxArea(height3)
    print(f"Test 3: height = {height3}")
    print(f"Expected: 2, Got: {result3}")
    assert result3 == 2, f"Test 3 failed: expected 2, got {result3}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
