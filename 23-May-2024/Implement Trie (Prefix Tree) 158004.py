# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class Trie:

    def __init__(self):
        self.root = TrieNode() 
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not curr.children[ord(c)-ord('a')]:
                curr.children[ord(c)-ord('a')] = TrieNode()
            curr = curr.children[ord(c)-ord('a')]
        curr.is_end = True       

        

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if not curr.children[ord(c)-ord('a')]:
                return False
            curr = curr.children[ord(c)-ord('a')]
        return curr.is_end

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if not curr.children[ord(c)-ord('a')]:
                return False
            curr = curr.children[ord(c)-ord('a')]
        return True


        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)