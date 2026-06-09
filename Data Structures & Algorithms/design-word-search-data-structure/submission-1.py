class trienode:
    def __init__(self, val = None):
        self.val = val
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = trienode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = trienode(char)
            curr = curr.children[char]
        curr.eow = True
        

    def search(self, word: str) -> bool:

        def find(i, node):
            curr = node
            for j in range(i, len(word)):
                c = word[j]
                if '.' == c:
                    for k in curr.children.values():
                        if find(j + 1, k):
                            return True

                    return False
                else:
                    if c not in curr.children:
                        return False

                    curr = curr.children[c]

            return curr.eow
            

        return find(0, self.root)