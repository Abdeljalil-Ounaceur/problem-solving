"""
LeetCode Problem 621: Task Scheduler
Difficulty: Medium
Topics: Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting

Problem Description:
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

Constraints:
1 <= tasks.length <= 10^4
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""
from typing import List
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Optimal solution using a mathematical formula.
        """
        counter = Counter(tasks)
        max_freq = max(counter.values())
        count_max_freq = sum(freq == max_freq for freq in counter.values())

        return max((max_freq - 1) * (n + 1) + count_max_freq, len(tasks))

    def leastInterval_alternative(self, tasks: List[str], n: int) -> int:
        """
        Alternative more programmatic less math solution using a max heap.
        """
        counter = Counter(tasks)
        
        # Max heap of frequencies (negative for max heap)
        max_heap = [-freq for freq in counter.values()]
        heapq.heapify(max_heap)
        
        time = 0
        cooldown = []  # [(available_time, freq)]
        
        while max_heap or cooldown:
            time += 1
            
            # Move tasks from cooldown back to heap if ready
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(max_heap, cooldown.pop(0)[1])
            
            # Execute most frequent available task
            if max_heap:
                freq = heapq.heappop(max_heap) + 1  # +1 because negative
                if freq != 0:
                    cooldown.append((time + n + 1, freq))
            # else: CPU is idle this cycle
        
        return time

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        (["A","A","A","B","B","B"], 2, 8),
        (["A","C","A","B","D","B"], 1, 6),
        (["A","A","A", "B","B","B"], 3, 10)
    ]
    
    for i, (tasks, n, expected) in enumerate(test_cases, 1):
        result_optimal = solution.leastInterval(tasks, n)
        result_alternative = solution.leastInterval_alternative(tasks, n)
        print(f"Test {i}:")
        print(f"  Optimal solution: {result_optimal}")
        print(f"  Alternative solution: {result_alternative}")
        print(f"  Expected: {expected}")
        assert result_optimal == expected
        assert result_alternative == expected
        print()
