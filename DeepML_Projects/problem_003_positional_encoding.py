"""
DeepML Problem #3: Positional Encoding Calculator
Difficulty: Hard
Category: Deep Learning

Problem Description:
Write a Python function to implement the Positional Encoding layer for Transformers. 
The function should calculate positional encodings for a sequence length (position) and 
model dimensionality (d_model) using sine and cosine functions as specified in the 
Transformer architecture. The function should return -1 if position is 0, or if d_model 
is less than or equal to 0. The output should be a numpy array of type float16.

Example:
Input:
position = 2, d_model = 8
Output:
[[[ 0.,0.,0.,0.,1.,1.,1.,1.,]
  [ 0.8413,0.0998,0.01,0.001,0.5405,0.995,1.,1.]]]

Reasoning:
The function computes the positional encoding by calculating sine values for even indices 
and cosine values for odd indices, ensuring that the encoding provides the required 
positional information.

Test Cases:
1. pos_encoding(2, 8) -> Expected specific sine/cosine pattern
2. pos_encoding(5, 16) -> Expected larger matrix with sine/cosine patterns

Contributors: Dripto Saha
"""

import numpy as np

def pos_encoding(position: int, d_model: int):
    """
    Implement positional encoding for Transformer architecture.
    
    Args:
        position (int): Sequence length
        d_model (int): Model dimensionality
        
    Returns:
        numpy.ndarray: Positional encoding matrix of shape (position, d_model) with dtype float16
        int: Returns -1 if position is 0 or d_model <= 0
    """
    # Handle edge cases
    if position == 0 or d_model <= 0:
        return -1

    # Create position indices (position, 1)
    pos = np.arange(position)[:, np.newaxis]

    # Create dimension indices (1, d_model//2) - we need half because sin and cos will double it
    i_ = np.arange(d_model // 2)[np.newaxis, :]

    # Calculate angle rates using the formula from "Attention Is All You Need" paper
    angle_rates = 1 / (10000 ** ((2 * i_) / d_model))

    # Broadcast multiplication: (position, 1) * (1, d_model//2) = (position, d_model//2)
    angles = pos * angle_rates

    # Apply sine and cosine functions
    sin_matrix = np.sin(angles)  # Shape: (position, d_model//2)
    cos_matrix = np.cos(angles)  # Shape: (position, d_model//2)

    # Initialize the final positional encoding matrix
    pos_encoding = np.zeros((position, d_model))
    
    # Fill even indices with sine values, odd indices with cosine values
    pos_encoding[:, 0::2] = sin_matrix  # even indices (0, 2, 4, ...)
    pos_encoding[:, 1::2] = cos_matrix  # odd indices (1, 3, 5, ...)

    # Convert to float16 as specified
    pos_encoding = np.float16(pos_encoding)
    
    return pos_encoding


# Test the function with provided test cases
if __name__ == "__main__":
    print("Testing Positional Encoding Calculator\n")
    
    # Test case 1: position=2, d_model=8
    print("Test 1: pos_encoding(2, 8)")
    result1 = pos_encoding(2, 8)
    print("Result:")
    print(result1)
    print("Expected pattern: sine/cosine alternating for 2 positions, 8 dimensions")
    print()
    
    # Test case 2: position=5, d_model=16
    print("Test 2: pos_encoding(5, 16)")
    result2 = pos_encoding(5, 16)
    print("Result:")
    print(result2)
    print("Expected pattern: sine/cosine alternating for 5 positions, 16 dimensions")
    print()
    
    # Test edge cases
    print("Test 3: Edge cases")
    print(f"pos_encoding(0, 8): {pos_encoding(0, 8)}")  # Should return -1
    print(f"pos_encoding(2, 0): {pos_encoding(2, 0)}")  # Should return -1
    print(f"pos_encoding(2, -1): {pos_encoding(2, -1)}")  # Should return -1
    print()
    
    # Verify output type and shape
    if isinstance(result1, np.ndarray):
        print(f"Output type: {type(result1)}")
        print(f"Output dtype: {result1.dtype}")
        print(f"Output shape for (2, 8): {result1.shape}")
        print(f"Output shape for (5, 16): {result2.shape}")
    
    print("\nPositional Encoding implementation complete!")
