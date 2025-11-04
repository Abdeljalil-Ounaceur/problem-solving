"""
127. Word Ladder
Solved
Hard
Topics
premium lock icon
Companies
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""

from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        
        L = len(beginWord)
        
        # Step 1: Build the adjacency map using patterns
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + '*' + word[i+1:]
                all_combo_dict[pattern].append(word)
        
        # Step 2: BFS
        queue = deque([(beginWord, 1)])  # (current_word, current_level)
        visited = set([beginWord])
        
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                pattern = current_word[:i] + '*' + current_word[i+1:]
                for neighbor in all_combo_dict[pattern]:
                    if neighbor == endWord:
                        return level + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                all_combo_dict[pattern] = []  # Clear to prevent revisiting
        return 0

# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    print(f"Input: beginWord = '{beginWord1}', endWord = '{endWord1}', wordList = {wordList1}")
    print(f"Output: {sol.ladderLength(beginWord1, endWord1, wordList1)}") # Expected: 5
    print("-" * 30)

    # Example 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    print(f"Input: beginWord = '{beginWord2}', endWord = '{endWord2}', wordList = {wordList2}")
    print(f"Output: {sol.ladderLength(beginWord2, endWord2, wordList2)}") # Expected: 0
    print("-" * 30)

    # Additional Test Case: No path
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a","b","d"]
    print(f"Input: beginWord = '{beginWord3}', endWord = '{endWord3}', wordList = {wordList3}")
    print(f"Output: {sol.ladderLength(beginWord3, endWord3, wordList3)}") # Expected: 0
    print("-" * 30)

    # Additional Test Case: Single step
    beginWord4 = "a"
    endWord4 = "b"
    wordList4 = ["b"]
    print(f"Input: beginWord = '{beginWord4}', endWord = '{endWord4}', wordList = {wordList4}")
    print(f"Output: {sol.ladderLength(beginWord4, endWord4, wordList4)}") # Expected: 2
    print("-" * 30)
