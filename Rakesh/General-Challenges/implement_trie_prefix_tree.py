__author__ = 'rakesh'

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current_dict = self.root.children
        for letter in word:
            current_dict= current_dict.setdefault(letter, {})
        current_dict[1]= 1
             #whether this word exists or not
        #just a status indicating whether the word exists or not

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current_dict = self.root.children
        for letter in word:
            current_dict = current_dict.get(letter)
            if current_dict is None:
                return False
        if current_dict.has_key(1):
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current_dict = self.root.children
        for letter in prefix:
            current_dict = current_dict.get(letter)
            if current_dict is None:
                return False
        return True
