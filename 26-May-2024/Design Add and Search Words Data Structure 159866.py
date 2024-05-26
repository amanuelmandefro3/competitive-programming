# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not curr.children[ord(c) - ord('a')]:
                curr.children[ord(c) - ord('a')] = TrieNode()
            curr = curr.children[ord(c) - ord('a')]
        curr.is_end = True  

    def search(self, word: str) -> bool:
        def dfs(idx, curr):
            if idx == len(word):
                return curr.is_end
            if word[idx] == '.':
                for i in range(26):
                    if curr.children[i] and dfs(idx + 1, curr.children[i]):
                        return True
            else:
                if curr.children[ord(word[idx]) - ord('a')]:
                    return dfs(idx + 1, curr.children[ord(word[idx]) - ord('a')])
            return False
        
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
