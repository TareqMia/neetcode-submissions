class TrieNode:

    def __init__(self, val=" "):
        self.val = " "
        self.children = {}
        self.isWord = False 


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        root = self.root
        for letter in word:
            if letter not in root.children:
                root.children[letter] = TrieNode(letter)
            root = root.children[letter]
        root.isWord = True
    
    def search(self, word: str) -> bool:
        root = self.root
        def dfs(index, root):
            curr = root 
            for i in range(index, len(word)): 
                c = word[i] 
                if c == ".":
                    # dfs 
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True 
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.isWord

        return dfs(0, root)
        
