class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        node = self.root

        for ch in word:

            if ch not in node.child:
                node.child[ch] = TrieNode()

            node = node.child[ch]

        node.end = True

    def search(self, word):

        node = self.root

        for ch in word:

            if ch not in node.child:
                return False

            node = node.child[ch]

        return node.end

trie = Trie()

n = int(input())

for _ in range(n):
    trie.insert(input())

print(trie.search(input()))