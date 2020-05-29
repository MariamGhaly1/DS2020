class Node:
    def __init__(self, char=''):
        self .char = char
        self.children = dict()
        self.isCompleteWord = False
        self.files = []


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word, file_num):
        current = self.root
        for i in range(len(word)):
            if word[i] not in current.children:
                current.children[word[i]] = Node(word[i])
            current = current.children[word[i]]
            if i == len(word)-1:
                current.isCompleteWord = True
                if file_num not in current.files:
                    current.files.append(file_num)

    def find(self, word):
        files = []
        current = self.root
        for char in word:
            if char not in current.children:
                return files
            current = current.children[char]
        if current.isCompleteWord:
            files = current.files
        return files

