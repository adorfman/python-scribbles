import json

class TrieNode:
    def __init__(self):
        self.children = {}

    @property
    def end(self):
        if not self.children:
             return True

        return False

    def print_level(self, key="root", level=0): 
        print(" "*level + key + "\n") 

        for child in self.children:
             node = self.children.get(child)
             node.print_level(child, level+1 ) 


    def all_words(self, prefix):
        if self.end:
            yield prefix

        for letter, child in self.children.items():
            yield from child.all_words(prefix + letter)

class Trie:

    def __init__(self):

        # Initialising the trie structure.
        self.root = TrieNode()

    # existing methods here
    def all_words_beginning_with_prefix(self, prefix):
        cur = self.root
        # Traverse tree to end of prefix or return none if we dont make it
        for c in prefix:
            cur = cur.children.get(c)
            if cur is None:
                return  # No words with given prefix

        yield from cur.all_words(prefix)


    def insert(self, key):

        # Inserts a key into trie if it does not exist already.
        # And if the key is a prefix of the trie node, just
        # marks it as leaf node.
        node = self.root

        for a in key:
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        #node.end = True

trie = Trie()
trie.insert('foobar')
trie.insert('foo')
trie.insert('bar')
trie.insert('foob')
trie.insert('foof')
trie.insert('foofar') 
trie.insert('foofun')  

print(list(trie.all_words_beginning_with_prefix('foof')))

gen = trie.all_words_beginning_with_prefix('foo');
print(next(gen));
print(next(gen));

trie.root.print_level()

