"""
LeetCode Problem #200: Number of Islands
Difficulty: Medium
Category: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix

Problem Description:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'

Test Cases:
1. Single island -> 1
2. Multiple islands -> 3
3. Empty grid -> 0
4. All water -> 0
5. All land -> 1

Contributors: u8tRAAB9Wu
"""

def find_adjacents(i, j, object_i, grid):
    """
    Recursive function to find adjacent land cells (DFS approach).
    This approach can cause timeout on large grids due to deep recursion.
    
    Args:
        i, j (int): Current position
        object_i (list): List to store connected land cells
        grid (List[List[str]]): The input grid
    """
    # Check up
    if (i-1 >= 0 and j >= 0 and i-1 < len(grid) and j < len(grid[0]) and grid[i-1][j] == "1"):
        if not (i-1, j) in object_i:
            object_i.append((i-1, j))
            find_adjacents(i-1, j, object_i, grid)
    
    # Check left
    if (i >= 0 and j-1 >= 0 and i < len(grid) and j-1 < len(grid[0]) and grid[i][j-1] == "1"):
        if not (i, j-1) in object_i:
            object_i.append((i, j-1))
            find_adjacents(i, j-1, object_i, grid)

    # Check down
    if (i+1 >= 0 and j >= 0 and i+1 < len(grid) and j < len(grid[0]) and grid[i+1][j] == "1"):
        if not (i+1, j) in object_i:
            object_i.append((i+1, j))
            find_adjacents(i+1, j, object_i, grid)
    
    # Check right
    if (i >= 0 and j+1 >= 0 and i < len(grid) and j+1 < len(grid[0]) and grid[i][j+1] == "1"):
        if not (i, j+1) in object_i:
            object_i.append((i, j+1))
            find_adjacents(i, j+1, object_i, grid)


class Solution(object):
    def numIslands_initial(self, grid):
        """
        Initial solution using recursive DFS with list tracking.
        This solution times out on large inputs due to inefficient tracking.
        
        Args:
            grid (List[List[str]]): 2D binary grid representing land/water
            
        Returns:
            int: Number of islands
        """
        if len(grid) == 0:
            return -1
        
        m = len(grid)
        n = len(grid[0])

        if (m < 1 or n < 1 or m > 300 or n > 300):
            return -1

        objects = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if len(objects) == 0:
                        objects.append([])
                        objects[0].append((i, j))
                        find_adjacents(i, j, objects[0], grid)
                    else: 
                        not_present = True
                        for object_i in objects:
                            for (I, J) in object_i:
                                if (i, j) == (I, J):
                                    not_present = False
                                    break
                            if not not_present:
                                break
                        if not_present:
                            objects.append([])
                            objects[-1].append((i, j))
                            find_adjacents(i, j, objects[-1], grid)
                
        return len(objects)

    def numIslands_optimized(self, grid):
        """
        Optimized solution using BFS with queue and in-place modification.
        This approach is more efficient as it marks visited cells as "0".
        
        Args:
            grid (List[List[str]]): 2D binary grid representing land/water
            
        Returns:
            int: Number of islands
        """
        if len(grid) == 0:
            return -1
        
        m = len(grid)
        n = len(grid[0])

        if (m < 1 or n < 1 or m > 300 or n > 300):
            return -1

        queue = []
        number_of_islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    number_of_islands += 1
                    queue.append((i, j))
                    grid[i][j] = "0"  # Mark as visited
                    
                    while queue:  # BFS to explore the entire island
                        current = queue.pop(0)
                        r, c = current
                        
                        # Check all four directions
                        if (r + 1 < m) and (grid[r + 1][c] == "1"):
                            grid[r + 1][c] = "0"
                            queue.append((r + 1, c))
                        if (c + 1 < n) and (grid[r][c + 1] == "1"):
                            grid[r][c + 1] = "0"
                            queue.append((r, c + 1))
                        if (r - 1 >= 0) and (grid[r - 1][c] == "1"):
                            grid[r - 1][c] = "0"
                            queue.append((r - 1, c))
                        if (c - 1 >= 0) and (grid[r][c - 1] == "1"):
                            grid[r][c - 1] = "0"
                            queue.append((r, c - 1))
            
        return number_of_islands

    def numIslands(self, grid):
        """
        Main solution method (using optimized version).
        
        Args:
            grid (List[List[str]]): 2D binary grid representing land/water
            
        Returns:
            int: Number of islands
        """
        return self.numIslands_optimized(grid)


# Test the solutions
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        # Test case 1: Single island
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ],
        # Test case 2: Multiple islands
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ],
        # Test case 3: Empty grid
        [],
        # Test case 4: All water
        [
            ["0","0","0"],
            ["0","0","0"],
            ["0","0","0"]
        ],
        # Test case 5: All land
        [
            ["1","1"],
            ["1","1"]
        ],
        # Test case 6: Single cell
        [["1"]]
    ]
    
    expected_results = [1, 3, 0, 0, 1, 1]
    
    print("Testing Number of Islands\n")
    
    for i, (test_case, expected) in enumerate(zip(test_cases, expected_results), 1):
        print(f"Test {i}: Expected {expected}")
        
        if test_case:  # Skip empty grid for initial solution
            # Create copies for testing
            grid_copy1 = [row[:] for row in test_case]
            grid_copy2 = [row[:] for row in test_case]
            
            # Test optimized solution
            result_optimized = solution.numIslands_optimized(grid_copy1)
            print(f"  Optimized Solution: {result_optimized}")
            
            # Test main solution
            result_main = solution.numIslands(grid_copy2)
            print(f"  Main Solution: {result_main}")
        else:
            print("  Empty grid - skipping initial solution test")
            result_optimized = solution.numIslands_optimized(test_case)
            print(f"  Optimized Solution: {result_optimized}")
        
        print(f"  Expected: {expected}")
        print()
    
    print("All tests completed!")
