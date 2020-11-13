#!/usr/bin/python3

# Cameron J. Calv
# Assignment 2
# CS260 Data Structures

# Project Problem 6: LevelOrder Tree Print
from loctree import loctree

# Accepts a tree as a parameter and returns the in-order of the tree's labels
# Assumes that the tree is not the Null tree
def levelorder(traversed_tree):
    # Traverse through the tree and add each node traversed the first time it is accessed to a
    # dictionary that contains a key for each level of the tree
    current_traversal_path = []
    levelorder_listing = {}
    levelorder_label_listing = {}
    leaf_found = 0
    current_level = 0
    next_node = traversed_tree.ROOT()
    while 1:
        node_label = traversed_tree.LABEL(next_node)
        current_traversal_path.append(next_node)
        if current_level not in levelorder_listing.keys():
            # Create a level in the ditionaries if it doesn't already exist
            levelorder_listing[current_level] = []
            levelorder_label_listing[current_level] = []
        if next_node not in levelorder_listing[current_level]:
            # Add each node to the level in the dictionary if it's not already there
            levelorder_listing[current_level].append(next_node)
            levelorder_label_listing[current_level].append(node_label)
        if (traversed_tree.LEFTMOST_CHILD(next_node) == 0):
            leaf_found = 1
        if leaf_found:
            del current_traversal_path[-1]
            if traversed_tree.RIGHT_SIBLING(next_node) == 0:
                next_node = traversed_tree.PARENT(next_node)
                current_level = current_level - 1
                leaf_found = 1
            else:
                next_node = traversed_tree.RIGHT_SIBLING(next_node)
                leaf_found = 0
        else:
            next_node = traversed_tree.LEFTMOST_CHILD(next_node)
            current_level = current_level + 1

        if next_node == traversed_tree.ROOT():
            break
    # Go back through the dictionary and add the labels as they appear for each level
    levelorder_traversal_list = []
    for level in levelorder_label_listing.keys():
        for node in levelorder_label_listing[level]:
            levelorder_traversal_list.append(node)
    return levelorder_traversal_list

if __name__ == '__main__':
    test_tree = loctree()
    print("Let's create a full level-3 tree of height 2 to test levelorder with nodes numbered from 1 to 13.")
    print("Creating tree...")
    node_2 = test_tree.CREATE3(2, test_tree.CREATE0(5), test_tree.CREATE0(6), test_tree.CREATE0(7))
    node_3 = test_tree.CREATE3(3, test_tree.CREATE0(8), test_tree.CREATE0(9), test_tree.CREATE0(10))
    node_4 = test_tree.CREATE3(4, test_tree.CREATE0(11), test_tree.CREATE0(12), test_tree.CREATE0(13))
    node_1 = test_tree.CREATE3(1, node_2, node_3, node_4)
    test_tree = node_1
    print("Test tree created!")
    print("Generating the levelorder listing of the tree...")
    test_levelorder = levelorder(test_tree)
    print("Levelorder listing created!")
    print(test_levelorder)
    print("Asserting the validity of the levelorder traversal...")
    x = 1
    for node in test_levelorder:
        assert (node == x)
        x = x + 1
    print("Levelorder test passed!")