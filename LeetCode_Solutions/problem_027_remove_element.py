"""
27. Remove Element
Difficulty: Easy
Topics: Array, Two Pointers

Problem Description:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are 
not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you 
need to do the following things:
- Change the array nums such that the first k elements of nums contain the elements which are 
  not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.

Custom Judge:
The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 
0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Optimal Solution: Two Pointers (In-Place Modification)
        
        Approach:
        - Use a write pointer (pos) to track where to place non-val elements
        - Iterate through the array with a read pointer (i)
        - When we find an element that is not equal to val, write it to the position
          indicated by pos and increment pos
        - Elements equal to val are simply skipped (not written)
        - Return pos, which represents the count of elements not equal to val
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - in-place modification with only constant extra space
        
        Key Insight:
        - We don't need to preserve the order of elements or worry about what comes 
          after the first k elements
        - By using a write pointer, we effectively compact all non-val elements to 
          the front of the array
        - This is similar to the partition step in quicksort
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pos] = nums[i]
                pos += 1
        return pos
