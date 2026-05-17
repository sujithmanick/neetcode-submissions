class Trie:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        ccurr_har = self.root
        for char in word:
            if char not in ccurr_har.children:
                ccurr_har.children[char] = Trie()
            ccurr_har = ccurr_har.children[char]
        ccurr_har.eow = True

        

    def search(self, word: str) -> bool:

        def dfs(j, node):
            curr = node

            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for val in curr.children.values():
                        if dfs(i + 1, val):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.eow
        return dfs(0, self.root)

        
