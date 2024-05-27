# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
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

    def find_root(self, word):
        curr = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if curr.children[index]:
                curr = curr.children[index]
                if curr.is_end:
                    return word[:i + 1]
            else:
                return word
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        successors = sentence.split()
        
        for i in range(len(successors)):
            root = trie.find_root(successors[i])
            successors[i] = root
        
        return ' '.join(successors)