"""
LeetCode Problem 139: Word Break
Difficulty: Medium
Topics: Array, Hash Table, String, Dynamic Programming, Trie, Memoization

Problem Description:
Given a string s and a dictionary of strings wordDict, return true if s can be segmented 
into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters.
- All the strings of wordDict are unique.
"""

from typing import List


class Solution:
    """
    Standard Textbook Solution - Bottom-up Dynamic Programming
    
    Approach:
    - Use a DP array where dp[i] represents whether s[0:i] can be segmented
    - dp[0] = True (empty string is always valid)
    - For each position i, check all possible splits j where 0 <= j < i
    - If dp[j] is True and s[j:i] is in wordDict, then dp[i] = True
    
    Time Complexity: O(n^2 * m) where n is length of s, m is average word length
    Space Complexity: O(n + w) where w is size of wordDict
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[len(s)]


class SolutionInitial:
    """
    Initial Solution - Forward Iteration with Possible Starts Tracking
    
    Approach:
    - Track all possible valid starting positions in the string
    - For each position, check if we can form a word from any valid start
    - Use max_word_len optimization to avoid checking unnecessarily long substrings
    - Early return when we reach the end of the string
    
    Time Complexity: O(n * k * m) where n is length of s, k is number of valid starts, 
                     m is average word length
    Space Complexity: O(n + w) where w is size of wordDict
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_word_len = max([len(word) for word in wordDict])
        possible_starts = {0}
        for i in range(len(s)):
            new_starts = []

            for start in possible_starts:
                if i+1-start > max_word_len:
                    continue

                if s[start:i+1] in wordDict:
                    if (i+1 == len(s)):
                        return True
                    new_starts.append(i+1)
            possible_starts.update(new_starts)

        return False


class SolutionOptimal:
    """
    Refined Solution - Optimized Forward Iteration with Early Pruning
    
    Approach:
    - Similar to initial solution but with better iteration strategy
    - For each valid start position, try extending to all possible ends
    - Use max word length to limit the search space
    - Skip positions that aren't valid starts (optimization)
    - Early return when we successfully segment the entire string
    
    Time Complexity: O(n * maxLen) where n is length of s, maxLen is max word length
    Space Complexity: O(n + w) where w is size of wordDict
    
    Performance: Even faster than the initial solution due to:
    1. Skipping invalid start positions early
    2. More efficient iteration pattern (extend from valid starts)
    3. Better cache locality when checking substrings
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        maxLen = max(map(len, wordDict))
        possible_starts = {0}

        for i in range(len(s)):
            if i not in possible_starts:
                continue

            # Try extending from this valid start
            for end in range(i + 1, min(len(s) + 1, i + maxLen + 1)):
                if s[i:end] in wordSet:
                    if end == len(s):
                        return True
                    possible_starts.add(end)

        return False


"""
Solution Comparison:

1. Standard Textbook Solution:
   - Classic DP approach, easy to understand
   - Checks all possible splits at each position
   - Time: O(n^2 * m), Space: O(n)
   
2. Initial Solution:
   - Forward iteration with possible starts tracking
   - Uses max_word_len optimization
   - Better performance on strings with many valid segmentations
   - Time: O(n * k * m), Space: O(n)
   
3. Optimal Solution:
   - Most efficient approach
   - Skips invalid positions early
   - Extends from valid starts only
   - Best performance overall
   - Time: O(n * maxLen), Space: O(n)

Key Insights:
- Converting wordDict to a set provides O(1) lookup
- Tracking max word length allows pruning of impossible substrings
- Early termination when reaching the end saves computation
- The optimal solution combines the best of both worlds: DP's correctness 
  with greedy forward iteration's efficiency
"""
