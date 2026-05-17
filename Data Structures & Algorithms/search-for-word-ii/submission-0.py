class Trienode:
    def __init__(self):
        self.children = {}
        self.eow = False


class Solution:
    def __init__(self):
        self.root = Trienode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        
        for w in words:
            curr = self.root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = Trienode()
                curr = curr.children[c]
            curr.eow = True

        visited, result = set(), set()

        def dfs(i, j, node, word):
            if i < 0 or j < 0  or i >= len(board) or j >= len(board[i]) or board[i][j] not in node.children or (i,j) in visited:
                return

            visited.add((i,j))
            node = node.children[board[i][j]]
            word+= board[i][j]
            if node.eow:
                result.add(word)

            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i, j - 1, node, word)

            visited.remove((i,j))



        
        for r in range(len(board)):
            for c in range(len(board[r])):
                dfs(r, c, self.root, "")

        return list(result)
 