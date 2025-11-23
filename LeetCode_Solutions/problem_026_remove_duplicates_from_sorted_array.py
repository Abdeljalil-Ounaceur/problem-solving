"""
LeetCode Problem #26: Remove Duplicates from Sorted Array
Difficulty: Easy
Topics: Array, Two Pointers

Problem:
Given an integer array nums sorted in non-decreasing order, remove the duplicates 
in-place such that each unique element appears only once. The relative order of 
the elements should be kept the same.

Consider the number of unique elements in nums to be k. After removing duplicates, 
return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. 
The remaining elements beyond index k - 1 can be ignored.

Custom Judge:
The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums 
being 1 and 2 respectively. It does not matter what you leave beyond the returned k 
(hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums 
being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the 
returned k (hence they are underscores).

Constraints:
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""

from typing import List

# ============================================================================
# Initial Solution - Using Set for Tracking
# ============================================================================
class Solution_Initial:
    """
    Approach: Use a set to track seen elements and write position pointer
    Time Complexity: O(n) where n is the length of nums
    Space Complexity: O(n) for the set storing unique elements
    
    This solution works but uses extra space for the set, which is not optimal
    given that the array is already sorted.
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        pos = 0
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
                nums[pos] = nums[i]
                pos += 1
        
        return pos


# ============================================================================
# Optimal Solution - Two Pointers
# ============================================================================
class Solution:
    """
    Approach: Use two pointers to track write position and compare adjacent elements
    Time Complexity: O(n) where n is the length of nums
    Space Complexity: O(1) - only using constant extra space
    
    Key insight: Since the array is sorted, duplicates are adjacent. We only need
    to compare each element with its previous element to detect duplicates.
    
    The 'pos' pointer tracks where to write the next unique element.
    We start from index 1 since the first element is always unique.
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        pos = 1  # Position to write next unique element
        for i in range(1, len(nums)):
            # If current element is different from previous, it's unique
            if nums[i] != nums[i - 1]:
                nums[pos] = nums[i]
                pos += 1
        
        return pos


# ============================================================================
# Test Cases
# ============================================================================
if __name__ == "__main__":
    # Test with both solutions
    solutions = [
        ("Initial (Set-based)", Solution_Initial()),
        ("Optimal (Two Pointers)", Solution())
    ]
    
    test_cases = [
        ([1, 1, 2], 2, [1, 2], "Basic case with one duplicate"),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4], "Multiple duplicates"),
        ([1], 1, [1], "Single element"),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5], "No duplicates"),
        ([1, 1, 1, 1, 1], 1, [1], "All duplicates"),
        ([-3, -1, 0, 0, 0, 3, 3], 4, [-3, -1, 0, 3], "Negative numbers"),
        ([1, 1, 2, 2, 3, 3], 3, [1, 2, 3], "All pairs of duplicates"),
    ]
    
    for name, solution in solutions:
        print(f"\n{'='*70}")
        print(f"Testing: {name}")
        print(f"{'='*70}")
        
        all_passed = True
        for nums_input, expected_k, expected_nums, description in test_cases:
            # Make a copy since the function modifies in-place
            nums = nums_input.copy()
            k = solution.removeDuplicates(nums)
            
            # Check if k matches expected
            k_match = k == expected_k
            # Check if first k elements match expected
            nums_match = nums[:k] == expected_nums
            
            status = "✓" if (k_match and nums_match) else "✗"
            if not (k_match and nums_match):
                all_passed = False
            
            print(f"{status} Input: {str(nums_input):35s} | k: {k} (expected: {expected_k}) | "
                  f"Result: {nums[:k]} | {description}")
            
            if not k_match:
                print(f"   ERROR: k mismatch - got {k}, expected {expected_k}")
            if not nums_match:
                print(f"   ERROR: array mismatch - got {nums[:k]}, expected {expected_nums}")
        
        print(f"\nResult: {'All tests passed! ✓' if all_passed else 'Some tests failed ✗'}")
