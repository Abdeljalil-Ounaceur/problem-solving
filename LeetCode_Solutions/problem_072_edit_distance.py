class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        LeetCode Problem #72: Edit Distance
        Difficulty: Medium
        Category: String, Dynamic Programming
        
        Given two strings word1 and word2, return the minimum number of operations 
        required to convert word1 to word2.
        
        You have the following three operations permitted on a word:
        - Insert a character
        - Delete a character  
        - Replace a character
        
        Example 1:
        Input: word1 = "horse", word2 = "ros"
        Output: 3
        Explanation: 
        horse -> rorse (replace 'h' with 'r')
        rorse -> rose (remove 'r')
        rose -> ros (remove 'e')
        
        Example 2:
        Input: word1 = "intention", word2 = "execution"
        Output: 5
        
        Constraints:
        0 <= word1.length, word2.length <= 500
        word1 and word2 consist of lowercase English letters.
        """
        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = 0 if word1[i - 1] == word2[j - 1] else 1

                dp[i][j] = min(
                    dp[i - 1][j] + 1,       # delete
                    dp[i][j - 1] + 1,       # insert
                    dp[i - 1][j - 1] + cost # replace / match
                )

        return dp[m][n]
