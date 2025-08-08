"""
DeepML Problem #1: Matrix-Vector Dot Product
Link: https://www.deep-ml.com/problems/1
Difficulty: Easy
Category: Linear Algebra
Status: Solved

Problem Description:
Write a Python function that computes the dot product of a matrix and a vector. 
The function should return a list representing the resulting vector if the operation 
is valid, or -1 if the matrix and vector dimensions are incompatible. A matrix 
(a list of lists) can be dotted with a vector (a list) only if the number of 
columns in the matrix equals the length of the vector. For example, an n x m 
matrix requires a vector of length m.

Example:
Input:
a = [[1, 2], [2, 4]], b = [1, 2]
Output:
[5, 10]
Reasoning:
Row 1: (1 * 1) + (2 * 2) = 1 + 4 = 5
Row 2: (1 * 2) + (2 * 4) = 2 + 8 = 10
"""

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    """
    Compute the dot product of a matrix and a vector.
    
    Args:
        a (list[list[int|float]]): Matrix represented as list of lists
        b (list[int|float]): Vector represented as a list
        
    Returns:
        list[int|float]: Resulting vector from matrix-vector dot product, or -1 if dimensions are incompatible
        
    Algorithm:
        1. Validate dimensions: matrix columns must equal vector length
        2. For each row in the matrix:
           - Multiply corresponding elements of row and vector
           - Sum the products to get the result for that row
        3. Return the resulting vector
        
    Time Complexity: O(n*m) where n is number of rows, m is number of columns
    Space Complexity: O(n) for the result vector
    """
    
    # Validate dimensions: matrix columns must equal vector length
    if len(a[0]) != len(b):
        return -1
    
    # Initialize result vector with zeros
    result = [0] * len(a)
    
    # Compute dot product for each row
    for i in range(len(a)):
        # For each row, multiply corresponding elements and sum
        result[i] = sum([b[j] * a[i][j] for j in range(len(b))])
    
    return result


# Test cases from DeepML platform
if __name__ == "__main__":
    # Test case 1: Float values
    print("Test 1:", matrix_dot_vector([[1.5, 2.5], [3.0, 4.0]], [2, 1]))
    # Expected: [5.5, 10.0] (1.5*2 + 2.5*1 = 5.5, 3.0*2 + 4.0*1 = 10.0)
    
    # Test case 2: Incompatible dimensions (should return -1)
    print("Test 2:", matrix_dot_vector([[1, 2], [2, 4], [6, 8], [12, 4]], [1, 2, 3]))
    # Expected: -1 (matrix has 2 columns but vector has 3 elements)
    
    # Test case 3: Valid 3x3 matrix with 3-element vector
    print("Test 3:", matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]))
    # Expected: [14, 25, 44]
    # Row 1: 1*1 + 2*2 + 3*3 = 1 + 4 + 9 = 14
    # Row 2: 2*1 + 4*2 + 5*3 = 2 + 8 + 15 = 25
    # Row 3: 6*1 + 8*2 + 9*3 = 6 + 16 + 27 = 49
