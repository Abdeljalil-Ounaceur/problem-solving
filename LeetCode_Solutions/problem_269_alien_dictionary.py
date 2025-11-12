class Solution:
    """
    LeetCode 269. Alien Dictionary
    Given a sorted dictionary (words sorted lexicographically by an unknown alien language),
    derive the order of the alphabet in that language.
    """
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        from collections import defaultdict, deque

        graph = defaultdict(set)
        indeg = {}
        # Build node set (all unique characters)
        for w in words:
            for c in w:
                indeg.setdefault(c, 0)
        # Build graph edges based on first difference
        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for a, b in zip(w1, w2):
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        indeg[b] += 1
                    break
        # BFS (Kahn's algorithm for topological sort)
        q = deque([c for c in indeg if indeg[c]==0])
        order = []
        while q:
            c = q.popleft()
            order.append(c)
            for nei in graph[c]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        return "" if len(order) < len(indeg) else ''.join(order)

if __name__ == "__main__":
    # Example 1:
    words1 = ["z","o"]
    print("Example 1 Output:", Solution().alienOrder(words1))  # Output: "zo"

    # Example 2:
    words2 = ["hrn","hrf","er","enn","rfnn"]
    print("Example 2 Output:", Solution().alienOrder(words2))  # Output should be a permutation of "hernf"

    # Invalid order case (prefix)
    words3 = ["abc", "ab"]
    print("Invalid case Output:", Solution().alienOrder(words3))  # Output: ""
