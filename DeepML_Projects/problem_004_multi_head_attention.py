"""
DeepML Problem #4: Implement Multi-Head Attention
Difficulty: Hard
Category: Deep Learning

Problem Description:
Implement the multi-head attention mechanism, a critical component of transformer models. 
Given Query (Q), Key (K), and Value (V) matrices, compute the attention outputs for 
multiple heads and concatenate the results.

Example:
Input:
Q = np.array([[1, 0], [0, 1]]), K = np.array([[1, 0], [0, 1]]), 
V = np.array([[1, 0], [0, 1]]), n_heads = 2
Output:
[[1., 0.], [0., 1.]]

Reasoning:
Multi-head attention is computed for 2 heads using the input Q, K, and V matrices. 
The resulting outputs for each head are concatenated to form the final attention output.

Test Cases:
1. Multi-head attention with 2 heads on 4x4 matrices
2. Multi-head attention with 4 heads on 6x8 matrices
3. Multi-head attention with 2 heads on 6x8 matrices

Contributors: nzomi
"""

import numpy as np
from scipy.special import softmax

def compute_qkv(X, W_q, W_k, W_v):
    """
    Compute Query, Key, and Value matrices from input X and weight matrices.
    
    Args:
        X (numpy.ndarray): Input matrix
        W_q (numpy.ndarray): Query weight matrix
        W_k (numpy.ndarray): Key weight matrix
        W_v (numpy.ndarray): Value weight matrix
        
    Returns:
        tuple: (Q, K, V) matrices
    """
    Q = X.dot(W_q)
    K = X.dot(W_k)
    V = X.dot(W_v)
    return Q, K, V

def self_attention(Q, K, V):
    """
    Compute self-attention mechanism.
    
    Args:
        Q (numpy.ndarray): Query matrix
        K (numpy.ndarray): Key matrix
        V (numpy.ndarray): Value matrix
        
    Returns:
        numpy.ndarray: Attention output
    """
    d_k = Q.shape[1]
    scores = Q.dot(K.T) / np.sqrt(d_k)
    weights = softmax(scores, axis=-1)
    attention = weights.dot(V)
    return attention

def multi_head_attention(Q, K, V, n_heads):
    """
    Implement multi-head attention mechanism.
    
    Args:
        Q (numpy.ndarray): Query matrix
        K (numpy.ndarray): Key matrix
        V (numpy.ndarray): Value matrix
        n_heads (int): Number of attention heads
        
    Returns:
        numpy.ndarray: Multi-head attention output
    """
    d_model = Q.shape[1]
    d_k = d_model // n_heads

    # Reshape and transpose to get shape (n_heads, batch, d_k)
    Q_reshaped = Q.reshape(Q.shape[0], n_heads, d_k)
    K_reshaped = K.reshape(K.shape[0], n_heads, d_k)
    V_reshaped = V.reshape(V.shape[0], n_heads, d_k)

    Q_transposed = Q_reshaped.transpose(1, 0, 2)
    K_transposed = K_reshaped.transpose(1, 0, 2)
    V_transposed = V_reshaped.transpose(1, 0, 2)

    heads = []
    for i in range(n_heads):
        head_i = self_attention(Q_transposed[i], K_transposed[i], V_transposed[i])
        heads.append(head_i)

    # Concatenate along feature dimension
    concatenated = np.concatenate(heads, axis=-1)
    return concatenated


# Test the function with provided test cases
if __name__ == "__main__":
    print("Testing Multi-Head Attention Implementation\n")
    
    # Test case 1: m=4, n=4, n_heads=2
    print("Test 1: 4x4 matrices with 2 heads")
    m, n = 4, 4
    n_heads = 2
    np.random.seed(42)
    X = np.arange(m*n).reshape(m,n)
    X = np.random.permutation(X.flatten()).reshape(m, n)
    W_q = np.random.randint(0,4,size=(n,n))
    W_k = np.random.randint(0,5,size=(n,n))
    W_v = np.random.randint(0,6,size=(n,n))
    Q, K, V = compute_qkv(X, W_q, W_k, W_v)
    result1 = multi_head_attention(Q, K, V, n_heads)
    print("Result:")
    print(result1)
    print("Expected: [[103, 109, 46, 99], [103, 109, 46, 99], [103, 109, 46, 99], [103, 109, 46, 99]]")
    print()
    
    # Test case 2: m=6, n=8, n_heads=4
    print("Test 2: 6x8 matrices with 4 heads")
    m, n = 6, 8
    n_heads = 4
    np.random.seed(42)
    X = np.arange(m*n).reshape(m,n)
    X = np.random.permutation(X.flatten()).reshape(m, n)
    W_q = np.random.randint(0,4,size=(n,n))
    W_k = np.random.randint(0,5,size=(n,n))
    W_v = np.random.randint(0,6,size=(n,n))
    Q, K, V = compute_qkv(X, W_q, W_k, W_v)
    result2 = multi_head_attention(Q, K, V, n_heads)
    print("Result:")
    print(result2)
    print("Expected: [[500, 463, 399, 495, 377, 450, 531, 362], [500, 463, 399, 495, 377, 450, 531, 362], [500, 463, 399, 495, 377, 450, 531, 362], [500, 463, 399, 495, 377, 450, 531, 362], [500, 463, 399, 495, 377, 450, 531, 362], [500, 463, 399, 495, 377, 450, 531, 362]]")
    print()
    
    # Test case 3: m=6, n=8, n_heads=2
    print("Test 3: 6x8 matrices with 2 heads")
    m, n = 6, 8
    n_heads = 2
    np.random.seed(42)
    X = np.arange(m*n).reshape(m,n)
    X = np.random.permutation(X.flatten()).reshape(m, n)
    W_q = np.random.randint(0,4,size=(n,n))
    W_k = np.random.randint(0,5,size=(n,n))
    W_v = np.random.randint(0,6,size=(n,n))
    Q, K, V = compute_qkv(X, W_q, W_k, W_v)
    result3 = multi_head_attention(Q, K, V, n_heads)
    print("Result:")
    print(result3)
    print("Expected: [[547, 490, 399, 495, 377, 450, 531, 362], [547, 490, 399, 495, 377, 450, 531, 362], [547, 490, 399, 495, 377, 450, 531, 362], [547, 490, 399, 495, 377, 450, 531, 362], [547, 490, 399, 495, 377, 450, 531, 362], [547, 490, 399, 495, 377, 450, 531, 362]]")
    print()
    
    print("All tests completed!")
