# 973. K Closest Points to Origin
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)² + (y1 - y2)²).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 
# Example 1:


# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 
# Constraints:

# 1 <= k <= points.length <= 104
# -104 <= xi, yi <= 104

from collections import defaultdict
from typing import List
from heapq import heappush, heappop

class Solution:
    """
    My solution
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        dist = defaultdict(list)
        for i in range(len(points)):
            distance = points[i][0]**2 + points[i][1]**2
            dist[distance].append(i)
        
        keys = sorted(dist.keys())
        for distance in keys:
            for index in dist[distance]:
                res.append(points[index])
                if len(res) == k:
                    return res

class OptimalSolution:
    """
    Optimal solution
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x,y in points:
            distance = x**2 + y**2
            heappush(res, (-distance, [x,y]))
            if len(res) > k:
                heappop(res)
        
        return [item[1] for item in res]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    optimal_solution = OptimalSolution()

    # Test case 1
    points1 = [[1,3],[-2,2]]
    k1 = 1
    print(f"Test 1: points = {points1}, k = {k1}")
    print(f"My solution: {solution.kClosest(points1, k1)}")
    print(f"Optimal solution: {optimal_solution.kClosest(points1, k1)}")
    print(f"Expected: [[-2,2]]\n")

    # Test case 2
    points2 = [[3,3],[5,-1],[-2,4]]
    k2 = 2
    print(f"Test 2: points = {points2}, k = {k2}")
    # The output order doesn't matter, so we sort the results for comparison
    my_sol_sorted = sorted(solution.kClosest(points2, k2))
    optimal_sol_sorted = sorted(optimal_solution.kClosest(points2, k2))
    expected_sorted = sorted([[3,3],[-2,4]])
    print(f"My solution: {my_sol_sorted}")
    print(f"Optimal solution: {optimal_sol_sorted}")
    print(f"Expected: {expected_sorted}\n")
