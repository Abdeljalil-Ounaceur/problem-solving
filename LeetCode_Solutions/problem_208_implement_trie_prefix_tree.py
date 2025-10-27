"""
LeetCode Problem #208: Implement Trie (Prefix Tree)
Difficulty: Medium
Category: Hash Table, String, Design, Trie

Problem Description:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, false otherwise.

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

Insert, search, and startsWith operate at O(m) time complexity where m is the key length.
Space complexity is O(total characters in all words) as we store every prefix.

Contributors: u8tRAAB9Wu
"""

class Trie:
    """
    Trie (Prefix Tree) implementation using dictionary nodes.

    Each node is a dictionary containing child nodes for each letter,
    and a terminal marker to indicate end of words.
    """

    def __init__(self):
        """
        Initializes the trie object with an empty root dictionary.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts the string word into the trie.

        Time Complexity: O(m) where m is the length of the word
        Space Complexity: O(m) for new nodes created

        Args:
            word (str): The word to insert into the trie
        """
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d[None] = True

    def search(self, word: str) -> bool:
        """
        Returns true if the string word is in the trie, false otherwise.

        Time Complexity: O(m) where m is the length of the word

        Args:
            word (str): The word to search for

        Returns:
            bool: True if word exists in trie, False otherwise
        """
        d = self.trie
        for c in word:
            if c not in d:
                return False
            d = d[c]

        if None not in d:
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns true if there is any previously inserted string word that has the prefix.

        Time Complexity: O(m) where m is the length of the prefix

        Args:
            prefix (str): The prefix to search for

        Returns:
            bool: True if any word starts with prefix, False otherwise
        """
        d = self.trie
        for c in prefix:
            if c not in d:
                return False
            d = d[c]

        return True


class TrieAlternative:
    """
    Alternative Trie implementation using "#" as end marker.

    This approach uses a dedicated end marker instead of None for
    clearer dictionary operations.
    """

    def __init__(self):
        """
        Initializes the trie object with an empty root dictionary.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts the string word into the trie.

        Time Complexity: O(m) where m is the length of the word
        Space Complexity: O(m) for new nodes created

        Args:
            word (str): The word to insert into the trie
        """
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d["#"] = True

    def search(self, word: str) -> bool:
        """
        Returns true if the string word is in the trie, false otherwise.

        Time Complexity: O(m) where m is the length of the word

        Args:
            word (str): The word to search for

        Returns:
            bool: True if word exists in trie, False otherwise
        """
        d = self.trie
        for c in word:
            if c not in d:
                return False
            d = d[c]

        return "#" in d

    def startsWith(self, prefix: str) -> bool:
        """
        Returns true if there is any previously inserted string word that has the prefix.

        Time Complexity: O(m) where m is the length of the prefix

        Args:
            prefix (str): The prefix to search for

        Returns:
            bool: True if any word starts with prefix, False otherwise
        """
        d = self.trie
        for c in prefix:
            if c not in d:
                return False
            d = d[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Test cases
def test_trie():
    """Test function to verify Trie implementation works correctly."""

    print("Testing Trie Implementation\n")

    # Test case 1: Basic functionality
    print("Test Case 1: Basic operations")
    trie1 = Trie()
    trie1.insert("apple")
    print(f"  insert('apple')")
    print(f"  search('apple'): {trie1.search('apple')}")  # Should be True
    print(f"  search('app'): {trie1.search('app')}")      # Should be False
    print(f"  startsWith('app'): {trie1.startsWith('app')}")  # Should be True
    trie1.insert("app")
    print(f"  insert('app')")
    print(f"  search('app'): {trie1.search('app')}")      # Should be True
    print()

    # Test case 2: Empty strings
    print("Test Case 2: Edge cases")
    trie2 = Trie()
    print(f"  search(''): {trie2.search('')}")    # Should be False (empty string not inserted)
    print(f"  startsWith(''): {trie2.startsWith('')}")  # Should be True (all strings start with empty string)
    print()

    # Test case 3: Multiple words and prefixes
    print("Test Case 3: Multiple words")
    trie3 = Trie()
    words = ["hello", "helium", "hero"]
    for word in words:
        trie3.insert(word)
        print(f"  insert('{word}')")

    print(f"  search('hello'): {trie3.search('hello')}")      # True
    print(f"  search('hel'): {trie3.search('hel')}")          # False
    print(f"  search('helium'): {trie3.search('helium')}")    # True
    print(f"  search('hero'): {trie3.search('hero')}")        # True
    print(f"  startsWith('he'): {trie3.startsWith('he')}")    # True
    print(f"  startsWith('hel'): {trie3.startsWith('hel')}")  # True
    print(f"  startsWith('hi'): {trie3.startsWith('hi')}")    # False
    print()

    # Test alternative implementation
    print("Testing Alternative Trie Implementation (using '#')")
    trie_alt = TrieAlternative()
    trie_alt.insert("cat")
    print(f"  insert('cat')")
    print(f"  search('cat'): {trie_alt.search('cat')}")      # True
    print(f"  search('ca'): {trie_alt.search('ca')}")        # False
    print(f"  startsWith('ca'): {trie_alt.startsWith('ca')}") # True

    print("\nAll tests completed!")


if __name__ == "__main__":
    test_trie()
