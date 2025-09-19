"""
LeetCode Problem 42: Trapping Rain Water
Difficulty: Hard
Topics: Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack

Problem Description:
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
"""

class Solution:
    def trap_unoptimized(self, height):
        """
        Unoptimized solution using stack approach.
        
        Time Complexity: O(n)
        Space Complexity: O(n) for the queue/stack
        
        The logic uses a queue to store (height, index) pairs and calculates
        trapped water by finding bounded areas between heights.
        """
        queue = []
        droplets = 0
        for i in range(len(height)):
            remainder = 0
            value = height[i]
            while(queue and value >= queue[-1][0]):
                _min = min(queue[-1][0], value) - remainder
                droplets += _min * (i - queue[-1][1] - 1)
                remainder = queue[-1][0]
                queue.pop()
                
            if(queue):
                _min = min(queue[-1][0], value) - remainder
                droplets += _min * (i - queue[-1][1] - 1)

            queue.append((value, i))
        
        return droplets

    def trap(self, height):
        """
        Optimized solution using monotonic stack.
        
        Time Complexity: O(n) - each element is pushed and popped at most once
        Space Complexity: O(n) for the stack in worst case
        
        Algorithm:
        1. Use a stack to store indices of heights in decreasing order
        2. When we find a height greater than or equal to the top of stack:
           - Pop the top (this is the bottom of potential water trap)
           - Calculate trapped water between current height and the new stack top
           - The width is the distance between current index and stack top
           - The height is the minimum of current height and stack top minus the bottom height
        3. Continue until stack is empty or current height is smaller than stack top
        4. Push current index to stack
        """
        stack = []
        droplets = 0
        
        for i in range(len(height)):
            # Process all heights in stack that are <= current height
            while stack and height[i] >= height[stack[-1]]:
                # Pop the top - this will be the bottom of the trapped water
                top = stack.pop()
                
                # If stack becomes empty, no left boundary exists
                if not stack:
                    break
                
                # Calculate trapped water
                # Height of trapped water = min of left and right boundaries - bottom height
                bounded_height = min(height[stack[-1]], height[i]) - height[top]
                # Width = distance between left boundary and current position - 1
                width = i - stack[-1] - 1
                droplets += bounded_height * width
            
            # Push current index to stack
            stack.append(i)
        
        return droplets

# Test cases
def test_solution():
    sol = Solution()
    
    # Test case 1
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    expected1 = 6
    result1_unopt = sol.trap_unoptimized(height1)
    result1_opt = sol.trap(height1)
    print(f"Test 1 - Input: {height1}")
    print(f"Expected: {expected1}, Unoptimized: {result1_unopt}, Optimized: {result1_opt}")
    assert result1_unopt == expected1, f"Unoptimized failed: expected {expected1}, got {result1_unopt}"
    assert result1_opt == expected1, f"Optimized failed: expected {expected1}, got {result1_opt}"
    
    # Test case 2
    height2 = [4,2,0,3,2,5]
    expected2 = 9
    result2_unopt = sol.trap_unoptimized(height2)
    result2_opt = sol.trap(height2)
    print(f"Test 2 - Input: {height2}")
    print(f"Expected: {expected2}, Unoptimized: {result2_unopt}, Optimized: {result2_opt}")
    assert result2_unopt == expected2, f"Unoptimized failed: expected {expected2}, got {result2_unopt}"
    assert result2_opt == expected2, f"Optimized failed: expected {expected2}, got {result2_opt}"
    
    # Test case 3 - Edge case
    height3 = [3,0,2,0,4]
    expected3 = 7
    result3_unopt = sol.trap_unoptimized(height3)
    result3_opt = sol.trap(height3)
    print(f"Test 3 - Input: {height3}")
    print(f"Expected: {expected3}, Unoptimized: {result3_unopt}, Optimized: {result3_opt}")
    assert result3_unopt == expected3, f"Unoptimized failed: expected {expected3}, got {result3_unopt}"
    assert result3_opt == expected3, f"Optimized failed: expected {expected3}, got {result3_opt}"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_solution()
