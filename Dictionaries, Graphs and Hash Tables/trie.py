#!/usr/bin/python3

# Cameron J. Calv
# Assignment 3
# CS260 Data Structures

# Project Problem 4: Trie Implementation and Insertion

import string
NULL_CHARACTER = '$'

class trieNode():

    # Uses a list representation to list the children of the trie node
    # Initializes a node to be a NULL node
    def __init__(self):
        self.chars = [letter for letter in string.ascii_uppercase]
        self.value = [NULL_CHARACTER]
        self.next = ["NULL"]
        return

    # Assigns the next pointer for child c in self.value to the position p
    # Assumes the character is part of the list of allowed characters
    def ASSIGN(self, c, p):
        if c in self.chars:
            index = 0
            for character in self.value:
                if character == c:
                    self.next[index] = p
                    return
                index = index + 1
            del self.value[-1]
            del self.next[-1]
            self.value.append(c)
            self.next.append(p)
            self.value.append(NULL_CHARACTER)
            self.next.append("NULL")
            return
        else:
            return

    # Returns the value of the next pointer for the given character c of the node
    # Returns NULL if the character is not a child of this node
    # Assumes the character is part of the list of allowed characters
    def VALUEOF(self, c):
        if c in self.chars:
            index = 0
            for character in self.value:
                if character == c:
                    return self.next[index]
                index = index + 1
            return "NULL"
        else:
            return "NULL"

    # Adds the character c to the list of children for this trie node
    # Assumes the character is part of the list of allowed characters
    def GETNEW(self, c):
        if c in self.chars:
            index = 0
            for character in self.value:
                if character == c:
                    self.next[index] = "NULL"
                    return
                index = index + 1
            del self.value[-1]
            del self.next[-1]
            self.value.append(c)
            self.next.append("NULL")
            self.value.append(NULL_CHARACTER)
            self.next.append("NULL")
            return
        else:
            return

    # Makes this node a NULL node (a leaf)
    def MAKENULL(self):
        self.value = [NULL_CHARACTER]
        self.next = ["NULL"]
        return

class trie():

    # Creates the trie with an initial root trie node that has no children
    def __init__(self):
        self.chars = [letter for letter in string.ascii_uppercase]
        self.root = 0
        self.nodes = []
        self.nodes.append(trieNode())

    # Return the pointer value referring to specific child of this node
    # corresponding to character x
    def VALUEOF(self, node, x):
        return node.VALUEOF(x)

    # Adds a new node to the trie if the current node doesn't already have a child
    # that corresponds to this letter
    def GETNEW(self, node, x):
        # Test if character is already a child of this node
        if node.VALUEOF(x) == "NULL":
            node.GETNEW(x)
            self.nodes.append(trieNode())
            node.ASSIGN(x, len(self.nodes)-1)
        else:
            return

    # Inserts the new word x into the set of words represented by the trie
    def INSERT(self, x):
        pointer = self.root
        word = x + NULL_CHARACTER
        word = word.upper()
        for character in word:
            if character in self.chars:
                # Test if node already has a child for current letter
                if self.VALUEOF(self.nodes[pointer], character) == "NULL":
                    self.GETNEW(self.nodes[pointer], character)
                pointer = self.nodes[pointer].VALUEOF(character)
            else:
                continue
        return

if __name__ == '__main__':
    test_trie = trie()
    filename = "alice30.txt"
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                test_trie.INSERT(word)
    print("The size of this Trie (Number of nodes it contains) is: "+str(len(test_trie.nodes)))
    num_of_words = 0
    for node in test_trie.nodes:
        if node.value[0] == NULL_CHARACTER:
            num_of_words = num_of_words + 1
    print("The size of this Trie (Number of words it contains) is: "+str(num_of_words))