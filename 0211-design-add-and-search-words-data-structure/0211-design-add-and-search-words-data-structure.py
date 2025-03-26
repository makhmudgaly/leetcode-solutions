class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TreeNode()
            node = node.children[c]
        
        node.is_word = True
        

    def search(self, word: str) -> bool:
        return self._search_helper(0, word, self.root)
        
    def _search_helper(self, word_index, word, node) -> bool:
        for i in range(word_index, len(word)):
            c = word[i]

            if c == '.':
                for child in node.children.values():
                    if self._search_helper(i + 1, word, child):
                        return True
                return False
            elif c in node.children:
                node = node.children[c]
            else:
                return False
            
        return node.is_word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)