"""
211. Design Add and Search Words Data Structure
Solved
Medium
Topics
premium lock icon
Companies
Hint
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""

class WordDictionary:
    """
    My initial solution using a Trie and iterative search with a list of candidates.
    """
    def __init__(self):
        self.trie = dict()
        

    def addWord(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d["END"] = True
            
    def search(self, word: str) -> bool:
        candidates = [self.trie]
        for c in word:
            if not candidates:
                return False

            new_candidates = []
            for candidate in candidates:
                if c == ".":
                    for child in candidate:
                        if child != "END" : new_candidates.append(candidate[child]) 
                elif c in candidate:
                    new_candidates.append(candidate[c])
            
            candidates = new_candidates

        return any("END" in d for d in candidates)

class WordDictionaryOptimal:
    """
    Optimal solution using a Trie and recursive DFS search.
    """
    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})
        node["#"] = True


    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return "#" in node
            
            c = word[i]
            if c == ".":
                return any(dfs(child, i + 1) for key, child in node.items() if key != "#")
            if c in node:
                return dfs(node[c], i + 1)
            return False

        return dfs(self.trie, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
