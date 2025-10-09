"""
210. Course Schedule II
Solved
Medium
Topics: Array, Depth-First Search, Breadth-First Search, Graph, Topological Sort
Companies: Amazon, Google, Facebook, Microsoft, Uber

Problem Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid 
answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished 
course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished 
both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Initial Solution - Complex approach with ordering dictionary
        
        This solution uses DFS with a complex ordering system that tracks the "depth" 
        of each course in the dependency graph. While it works, it's unnecessarily 
        complicated and less efficient.
        
        Time Complexity: O(V + E) where V is numCourses and E is len(prerequisites)
        Space Complexity: O(V + E) for the graph, orders dict, and recursion stack
        
        The approach:
        1. Build adjacency list representation of the graph
        2. Use DFS to detect cycles and calculate "order" (depth) for each course
        3. Sort courses by their calculated order and reverse to get topological order
        """
        orders = {}
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visiting = set()   

        def dfs(course):
            if not graph[course]:
                orders[course] = 0
                return 0

            if course in visiting:
                return None 

            if course in orders:
                return orders[course] 

            visiting.add(course)
            for next_course in graph[course]:
                if dfs(next_course) is None:
                    return None
            visiting.remove(course)
            orders[course] = 1 + max([orders[next_course] for next_course in graph[course]])
            return orders[course]

        for c in range(len(graph)):
            if dfs(c) is None:
                return []
        
        orders = dict(sorted(orders.items(), key=lambda item:item[1]))
        
        return list(reversed(orders.keys()))


class OptimalSolution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Optimal Solution - Clean DFS with Topological Sort
        
        This is the standard approach for topological sorting using DFS. It's much 
        cleaner and more intuitive than the initial solution.
        
        Time Complexity: O(V + E) where V is numCourses and E is len(prerequisites)
        Space Complexity: O(V + E) for the graph, sets, and recursion stack
        
        The approach:
        1. Build adjacency list representation of the graph
        2. Use DFS with three states: unvisited, visiting (gray), visited (black)
        3. Detect cycles by checking if we encounter a "visiting" node
        4. Add nodes to result in post-order (after processing all dependencies)
        5. Reverse the result to get correct topological order
        
        Key insight: In DFS post-order traversal, a node is added to result only 
        after all its dependencies have been processed, so reversing gives us the 
        correct topological order.
        """
        result = []
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course) 

        visited = set()    # Black nodes - completely processed
        visiting = set()   # Gray nodes - currently being processed

        def dfs(course):
            if course in visiting:
                return False  # Cycle detected
            if course in visited:
                return True   # Already processed

            visiting.add(course)
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            visiting.remove(course)
            visited.add(course)
            result.append(course)  # Post-order: add after processing dependencies
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return result[::-1]  # Reverse to get correct topological order


# Test cases
def test_solutions():
    solution = Solution()
    optimal = OptimalSolution()
    
    # Test case 1
    numCourses1 = 2
    prerequisites1 = [[1,0]]
    expected1 = [0,1]
    result1 = solution.findOrder(numCourses1, prerequisites1)
    optimal1 = optimal.findOrder(numCourses1, prerequisites1)
    print(f"Test 1 - Initial: {result1}, Optimal: {optimal1}, Expected: {expected1}")
    
    # Test case 2
    numCourses2 = 4
    prerequisites2 = [[1,0],[2,0],[3,1],[3,2]]
    result2 = solution.findOrder(numCourses2, prerequisites2)
    optimal2 = optimal.findOrder(numCourses2, prerequisites2)
    print(f"Test 2 - Initial: {result2}, Optimal: {optimal2}")
    
    # Test case 3
    numCourses3 = 1
    prerequisites3 = []
    expected3 = [0]
    result3 = solution.findOrder(numCourses3, prerequisites3)
    optimal3 = optimal.findOrder(numCourses3, prerequisites3)
    print(f"Test 3 - Initial: {result3}, Optimal: {optimal3}, Expected: {expected3}")
    
    # Test case 4 - Cycle detection
    numCourses4 = 2
    prerequisites4 = [[1,0],[0,1]]
    expected4 = []
    result4 = solution.findOrder(numCourses4, prerequisites4)
    optimal4 = optimal.findOrder(numCourses4, prerequisites4)
    print(f"Test 4 (Cycle) - Initial: {result4}, Optimal: {optimal4}, Expected: {expected4}")


if __name__ == "__main__":
    test_solutions()
