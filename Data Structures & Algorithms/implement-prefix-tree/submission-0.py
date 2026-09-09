class TrieNode:
    def __init__(self, val=' '):
        self.val = val 
        self.children = [None] * 26 
        self.isWord = False 

class PrefixTree:


    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        root = self.root 

        for c in word:
            index = ord(c) - ord('a')
            if root and root.children[index] is None:
                root.children[index] = TrieNode(c)
            root = root.children[index]
        root.isWord = True
                

    def search(self, word: str) -> bool:
        root = self.root 
        for c in word:
            index = ord(c) - ord('a')
            if root and root.children[index] is None:
                return False 
            root = root.children[index]

        return root.isWord
        
    def startsWith(self, prefix: str) -> bool:
        root = self.root 
        for c in prefix:
            index = ord(c) - ord('a')
            if root and root.children[index] is None:
                return False 
            root = root.children[index]

        return True

        
        