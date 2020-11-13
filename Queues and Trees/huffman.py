#!/usr/bin/python3

# Cameron J. Calv
# Assignment 2
# CS260 Data Structures

# Project Problem 9: Huffman Code Determination

from loctree import loctree


# Takes a list of trees as a parameter and returns the list sorted
# with respect to the value of the roots of the trees
def sortTrees(list_of_trees):
    final_length = len(list_of_trees)
    sorted_trees = []
    while (len(sorted_trees) != final_length):
        current_min_index = 0
        current_min = list_of_trees[0]
        for index in range(len(list_of_trees)):
            tree = list_of_trees[index]
            tree_value = tree.LABEL(tree.ROOT())
            min_value = current_min.LABEL(current_min.ROOT())
            if tree_value < min_value:
                current_min = tree
                current_min_index = index
        sorted_trees.append(current_min)
        del (list_of_trees[current_min_index])
    return sorted_trees


# Returns the Huffman Tree associated with the given characters and frequencies
# Assumes a dictionary is provided with frequency keys and character values
# Assumes that frequencies add up to a total of 100
def huffman(frequencies_and_characters):
    frequencies = []
    null_tree = loctree()
    # Prepare a list of frequencies to create the huffman tree based off of
    for frequency in frequencies_and_characters.keys():
        frequencies.append(frequency)
    frequencies.sort()
    huffman_tree_frequencies = []
    # Create a rough collection of nodes for the huffman tree
    for frequency in frequencies:
        huffman_tree_frequencies.append(null_tree.CREATE0(frequency))
    # Repeat process until the huffman tree list is a single tree
    while len(huffman_tree_frequencies) != 1:
        # Take the first two values and combine them
        first_node = huffman_tree_frequencies[0]
        second_node = huffman_tree_frequencies[1]
        first_value = first_node.LABEL(first_node.ROOT())
        second_value = second_node.LABEL(second_node.ROOT())
        code_node = null_tree.CREATE2(first_value + second_value, first_node, second_node)
        binary_node = null_tree.CREATE2(first_value + second_value, null_tree.CREATE0(1), null_tree.CREATE0(0))
        # Delete the two values from the huffman tree
        del (huffman_tree_frequencies[0])
        del (huffman_tree_frequencies[0])
        # Add the combined value back to the huffman tree
        huffman_tree_frequencies.append(code_node)
        # Sort the huffman tree and start over
        huffman_tree_frequencies = sortTrees(huffman_tree_frequencies)
    # Traverse back through the huffman tree and determine the codes for each character
    huffman_tree = huffman_tree_frequencies[0]
    code_string = []
    codes_and_characters = {}
    leaf_found = 0
    next_node = huffman_tree.ROOT()
    while len(codes_and_characters.keys()) != len(frequencies_and_characters.keys()):
        node_label = huffman_tree.LABEL(next_node)
        if (node_label in frequencies) and (huffman_tree.LEFTMOST_CHILD(next_node) == 0):
            code = ''
            for bit in code_string:
                code = code + bit
            codes_and_characters[code] = frequencies_and_characters[node_label]
            leaf_found = 1
        if leaf_found:
            del code_string[-1]
            if huffman_tree.RIGHT_SIBLING(next_node) == 0:
                next_node = huffman_tree.PARENT(next_node)
                leaf_found = 1
            else:
                code_string.append('1')
                next_node = huffman_tree.RIGHT_SIBLING(next_node)
                leaf_found = 0
        else:
            code_string.append('0')
            next_node = huffman_tree.LEFTMOST_CHILD(next_node)
    for code in codes_and_characters.keys():
        print(code, " : ", codes_and_characters[code])
    print(huffman_tree_frequencies[0].header)
    print(huffman_tree_frequencies[0].labels)
    print(huffman_tree_frequencies[0].root)
    return huffman_tree


if __name__ == '__main__':
    print("Let's set up our Huffman Tree with certain characters and frequencies!")
    print("'a' : 7%\n'b' : 9%\n'c' : 12%\n'd' : 22%\n'e' : 23%\n'f' : 27%")
    print("Running the Huffman program and printing out codes...")
    frequencies_and_characters = {7: 'a', 9: 'b', 12: 'c', 22: 'd', 23: 'e', 27: 'f'}
    characters_and_frequencies = {'a': 7, 'b': 9, 'c': 12, 'd': 22, 'e': 23, 'f': 27}
    test_huffman = huffman(frequencies_and_characters)
    print("Confirming some code samples in tree...")
    node_d = test_huffman.LEFTMOST_CHILD(test_huffman.LEFTMOST_CHILD(test_huffman.ROOT()))
    assert (test_huffman.LABEL(node_d) == characters_and_frequencies['d'])
    node_f = test_huffman.LEFTMOST_CHILD(test_huffman.RIGHT_SIBLING(test_huffman.LEFTMOST_CHILD(test_huffman.ROOT())))
    assert (test_huffman.LABEL(node_f) == characters_and_frequencies['f'])
    node_a = test_huffman.LEFTMOST_CHILD(test_huffman.RIGHT_SIBLING(
        test_huffman.LEFTMOST_CHILD(test_huffman.RIGHT_SIBLING(
            test_huffman.LEFTMOST_CHILD(test_huffman.RIGHT_SIBLING(
                test_huffman.LEFTMOST_CHILD(test_huffman.ROOT())))
        ))
    ))
    assert (test_huffman.LABEL(node_a) == characters_and_frequencies['a'])
    print("Huffman Codes confirmed!")