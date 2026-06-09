class trienode:
    def __init__(self, val = None):
        self.val = val
        self.children = {}
        self.eow = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = trienode()
        for l in words:
            curr = root
            for m in l:
                if m not in curr.children:
                    curr.children[m] = trienode(m)
                curr = curr.children[m]
            curr.eow = True

        res = set()
        visited = set()
        def track(curr, word, i,j):

            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] not in curr.children or (i,j) in visited:
                return

            
                
            visited.add((i,j))
            curr = curr.children[board[i][j]]
            word+= board[i][j]

            if curr.eow:
                res.add(word)

            track(curr, word, i,j + 1)
            track(curr, word, i,j - 1)
            track(curr, word, i + 1,j)
            track(curr, word, i - 1,j)

            visited.remove((i,j))
            

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                track(root,"", i,j)

        return list(res)