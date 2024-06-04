# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True

    def created_from_other(self, word):
        curr = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not curr.children[index] or not curr.children[index].is_end:
                return False
            curr = curr.children[index]
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = ""
        for word in words:
            if trie.created_from_other(word):
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    res = word

        return res