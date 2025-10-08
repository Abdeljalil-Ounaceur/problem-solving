"""
LeetCode Problem 207: Course Schedule
Difficulty: Medium
Topics: Depth-First Search, Breadth-First Search, Graph, Topological Sort

Problem Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you 
must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also 
have finished course 1. So it is impossible.

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.
"""

from typing import List
from collections import deque


# ============================================================================
# Initial Solution - Cycle Detection with Recurrence Stack
# ============================================================================
# Time Complexity: O(V + E) where V is numCourses and E is prerequisites length
# Space Complexity: O(V + E) for adjacency list and recursion stack
# 
# Approach: Build a dependency graph where each course points to its prerequisites.
# Use DFS with a recurrence stack to detect cycles. If a cycle exists, it's impossible
# to finish all courses.
#
# Note: This solution is correct but slightly slower due to recreating the recStack
# for each starting node in the main loop.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        deps = {i: [] for i in range(numCourses)}
        visited = set()

        for [course_id, req_id] in prerequisites:
            deps[course_id].append(req_id)

        def isCyclic(deps, i, visited, recStack):
            if i in recStack:
                return True
            if i in visited:
                return False

            visited.add(i)
            recStack.add(i)

            for adj in deps[i]:
                if isCyclic(deps, adj, visited, recStack):
                    return True

            recStack.remove(i)
            return False

        for i in deps:
            if i in visited:
                continue
            if isCyclic(deps, i, set(), set()):
                return False
            
        return True


# ============================================================================
# Optimal Solution - DFS with Visiting/Visited States
# ============================================================================
# Time Complexity: O(V + E) where V is numCourses and E is prerequisites length
# Space Complexity: O(V + E) for adjacency list and recursion stack
# 
# Approach: Build a directed graph where prerequisites point to dependent courses
# (reversed from initial solution). Use DFS with two sets:
# - visiting: tracks nodes in current DFS path (detects back edges/cycles)
# - visited: tracks completely processed nodes (optimization to avoid reprocessing)
#
# Key optimization: The graph is built in reverse direction (prereq -> course)
# and we maintain visiting/visited sets globally, allowing better pruning.
class SolutionOptimal:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # Reversed: prereq points to courses that depend on it

        visited = set()    # Fully processed nodes
        visiting = set()   # Nodes in current DFS path

        def dfs(course):
            if course in visiting:
                return False  # Back edge detected - cycle found
            if course in visited:
                return True   # Already processed this node and its descendants

            visiting.add(course)
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


# ============================================================================
# Test Cases
# ============================================================================
if __name__ == "__main__":
    solution = Solution()
    solution_optimal = SolutionOptimal()

    # Test Case 1
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    print(f"Test 1 - Initial: {solution.canFinish(numCourses1, prerequisites1)}")  # Expected: True
    print(f"Test 1 - Optimal: {solution_optimal.canFinish(numCourses1, prerequisites1)}")  # Expected: True

    # Test Case 2
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    print(f"Test 2 - Initial: {solution.canFinish(numCourses2, prerequisites2)}")  # Expected: False
    print(f"Test 2 - Optimal: {solution_optimal.canFinish(numCourses2, prerequisites2)}")  # Expected: False

    # Test Case 3: Multiple dependencies
    numCourses3 = 4
    prerequisites3 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(f"Test 3 - Initial: {solution.canFinish(numCourses3, prerequisites3)}")  # Expected: True
    print(f"Test 3 - Optimal: {solution_optimal.canFinish(numCourses3, prerequisites3)}")  # Expected: True

    # Test Case 4: No prerequisites
    numCourses4 = 3
    prerequisites4 = []
    print(f"Test 4 - Initial: {solution.canFinish(numCourses4, prerequisites4)}")  # Expected: True
    print(f"Test 4 - Optimal: {solution_optimal.canFinish(numCourses4, prerequisites4)}")  # Expected: True
