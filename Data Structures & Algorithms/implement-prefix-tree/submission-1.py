class TrieNode:
    def __init__(self):
        self.children = {}
        self.eot = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

        

    def insert(self, word: str) -> None:
        trie = self.root
        for char in word:
            if char not in trie.children:
                trie.children[char] = TrieNode()
            trie = trie.children[char]
        trie.eot = True
        


    def search(self, word: str) -> bool:
        trie = self.root
        for char in word:
            if char not in trie.children:
                return False
            trie = trie.children[char]
        return trie.eot
        

    def startsWith(self, prefix: str) -> bool:

        trie = self.root
        for char in prefix:
            if char not in trie.children:
                return False
            trie = trie.children[char]
        return True
        
        
        