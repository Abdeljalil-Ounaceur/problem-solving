"""
LeetCode Problem #146: LRU Cache
Difficulty: Medium
Category: Hash Table, Linked List, Design, Doubly-Linked List

Problem Description:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, 
  add the key-value pair to the cache. If the number of keys exceeds the capacity from 
  this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example:
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.

Test Cases:
1. Basic operations with capacity 2
2. Capacity 1 with multiple puts
3. Large capacity operations
4. Edge cases with invalid capacity

Contributors: u8tRAAB9Wu
"""

from collections import OrderedDict

class LRUCache(object):
    """
    LRU Cache implementation using OrderedDict for O(1) operations.
    
    Runtime: 95ms (Beats 94.57%)
    Memory: 77.89MB (Beats 93.73%)
    """

    def __init__(self, capacity):
        """
        Initialize the LRU cache with given capacity.
        
        Args:
            capacity (int): Maximum number of key-value pairs the cache can hold
            
        Raises:
            ValueError: If capacity is not within valid range [1, 3000]
        """
        if capacity < 1 or capacity > 3000:
            raise ValueError("capacity value not supported")
        
        self.capacity = capacity
        self.dictionary = OrderedDict()
        self.access_count = 0

    def get(self, key):
        """
        Get the value for the given key and mark it as most recently used.
        
        Args:
            key (int): The key to look up
            
        Returns:
            int: The value associated with the key, or -1 if key doesn't exist
        """
        if key in self.dictionary:
            # Move to end to mark as most recently used
            self.dictionary.move_to_end(key)
            return self.dictionary[key]
        else:
            return -1

    def put(self, key, value):
        """
        Add or update a key-value pair in the cache.
        If capacity is exceeded, remove the least recently used item.
        
        Args:
            key (int): The key to add/update
            value (int): The value to associate with the key
        """
        # If key doesn't exist and we're at capacity, remove LRU item
        if key not in self.dictionary and len(self.dictionary) >= self.capacity:
            # Remove the least recently used item (first item in OrderedDict)
            self.dictionary.popitem(last=False)

        # Add/update the key-value pair
        self.dictionary[key] = value
        # Move to end to mark as most recently used
        self.dictionary.move_to_end(key)


# Test the LRU Cache implementation
if __name__ == "__main__":
    print("Testing LRU Cache Implementation\n")
    
    # Test case 1: Basic operations with capacity 2
    print("Test 1: Basic operations with capacity 2")
    try:
        lru = LRUCache(2)
        print("  Created LRU Cache with capacity 2")
        
        lru.put(1, 1)
        print("  put(1, 1) - cache: {1=1}")
        
        lru.put(2, 2)
        print("  put(2, 2) - cache: {1=1, 2=2}")
        
        result = lru.get(1)
        print(f"  get(1) = {result} (expected: 1)")
        
        lru.put(3, 3)
        print("  put(3, 3) - LRU key 2 evicted, cache: {1=1, 3=3}")
        
        result = lru.get(2)
        print(f"  get(2) = {result} (expected: -1)")
        
        lru.put(4, 4)
        print("  put(4, 4) - LRU key 1 evicted, cache: {3=3, 4=4}")
        
        result = lru.get(1)
        print(f"  get(1) = {result} (expected: -1)")
        
        result = lru.get(3)
        print(f"  get(3) = {result} (expected: 3)")
        
        result = lru.get(4)
        print(f"  get(4) = {result} (expected: 4)")
        
    except Exception as e:
        print(f"  Error: {e}")
    
    print()
    
    # Test case 2: Capacity 1
    print("Test 2: Capacity 1")
    try:
        lru = LRUCache(1)
        print("  Created LRU Cache with capacity 1")
        
        lru.put(1, 1)
        print("  put(1, 1)")
        
        lru.put(2, 2)
        print("  put(2, 2) - key 1 evicted")
        
        result = lru.get(1)
        print(f"  get(1) = {result} (expected: -1)")
        
        result = lru.get(2)
        print(f"  get(2) = {result} (expected: 2)")
        
    except Exception as e:
        print(f"  Error: {e}")
    
    print()
    
    # Test case 3: Invalid capacity
    print("Test 3: Invalid capacity")
    try:
        lru = LRUCache(0)  # Should raise ValueError
        print("  Created LRU Cache with capacity 0 (unexpected)")
    except ValueError as e:
        print(f"  Correctly raised ValueError: {e}")
    except Exception as e:
        print(f"  Unexpected error: {e}")
    
    try:
        lru = LRUCache(3001)  # Should raise ValueError
        print("  Created LRU Cache with capacity 3001 (unexpected)")
    except ValueError as e:
        print(f"  Correctly raised ValueError: {e}")
    except Exception as e:
        print(f"  Unexpected error: {e}")
    
    print()
    print("All tests completed!")
