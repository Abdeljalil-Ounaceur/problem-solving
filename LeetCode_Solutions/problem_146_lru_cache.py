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
"""

# Optimal Solution: From-scratch implementation with dummy head/tail nodes
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node):
        # always add right before tail
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            # evict from head
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

# Initial Solution: From-scratch implementation with explicit tail pointer
class NodeInitial:
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt

class LRUCacheInitial:

    def __init__(self, capacity: int):
        self.cache = {}                # key -> Node
        self.queue = NodeInitial(-1, -1)      # dummy head
        self.last = self.queue         # tail pointer (initially dummy)
        self.capacity = capacity
        self.count = 0

    def _append_at_tail(self, node):
        """Append a node at the tail (assumes node is detached)."""
        node.prev = self.last
        node.next = None
        self.last.next = node
        self.last = node

    def move_to_last(self, node):
        """Move an existing node to the tail (most recent)."""
        if self.last is node:
            return  # already tail
        # detach node
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        # append at tail
        self._append_at_tail(node)

    def replace_least_used(self, key, val):
        """Evict least-recently-used (right after dummy head) then insert new (key,val)."""
        old = self.queue.next
        if not old:
            # nothing to evict (shouldn't happen if capacity > 0 and count==capacity)
            return
        # unlink old from head
        self.queue.next = old.next
        if old.next:
            old.next.prev = self.queue
        else:
            # if old was also the tail, we need to move tail back to dummy
            # (but since we will append a new node immediately, last will be updated there)
            self.last = self.queue

        # remove from dict
        self.cache.pop(old.key, None)

        # create and append new node; keep count the same (evict then insert)
        new = NodeInitial(key, val)
        self._append_at_tail(new)
        self.cache[key] = new
        # count stays unchanged

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key] # Corrected: selfself.cache[key] to self.cache[key]
        self.move_to_last(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_last(node)
            return

        if self.count == self.capacity:
            # evict LRU and insert new node (keeps count constant)
            self.replace_least_used(key, value)
            return

        # normal insertion (space available)
        new = NodeInitial(key, value)
        self._append_at_tail(new)
        self.cache[key] = new
        self.count += 1


# Test the LRU Cache implementation
if __name__ == "__main__":
    print("Testing LRU Cache Implementation\n")

    def run_test(cache_class):
        print(f"--- Testing {cache_class.__name__} ---")
        try:
            lru = cache_class(2)
            print("  Created LRU Cache with capacity 2")
            
            lru.put(1, 1)
            print("  put(1, 1)")
            
            lru.put(2, 2)
            print("  put(2, 2)")
            
            result = lru.get(1)
            print(f"  get(1) -> {result} (expected: 1)")
            assert result == 1

            lru.put(3, 3)
            print("  put(3, 3)")
            
            result = lru.get(2)
            print(f"  get(2) -> {result} (expected: -1)")
            assert result == -1

            lru.put(4, 4)
            print("  put(4, 4)")
            
            result = lru.get(1)
            print(f"  get(1) -> {result} (expected: -1)")
            assert result == -1

            result = lru.get(3)
            print(f"  get(3) -> {result} (expected: 3)")
            assert result == 3

            result = lru.get(4)
            print(f"  get(4) -> {result} (expected: 4)")
            assert result == 4
            print("  Test Passed!")
        except Exception as e:
            print(f"  Test Failed: {e}")
        print()

    run_test(LRUCache)
    run_test(LRUCacheInitial)

    print("All tests completed!")