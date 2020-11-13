#!/usr/bin/python3

# Cameron J. Calv
# Assignment 2
# CS260 Data Structures

# Project Problem NULL: PreOrder Tree Print
from loctree import loctree


def preorder(traversed_tree):
    # Traverse back through the huffman tree and determine the codes for each character
    current_traversal_path = []
    preorder_listing = []
    preorder_label_listing = []
    leaf_found = 0
    next_node = traversed_tree.ROOT()
    while 1:
        node_label = traversed_tree.LABEL(next_node)
        current_traversal_path.append(next_node)
        if next_node not in preorder_listing:
            preorder_listing.append(next_node)
            preorder_label_listing.append(node_label)
        if (traversed_tree.LEFTMOST_CHILD(next_node) == 0):
            leaf_found = 1
        if leaf_found:
            del current_traversal_path[-1]
            if traversed_tree.RIGHT_SIBLING(next_node) == 0:
                next_node = traversed_tree.PARENT(next_node)
                leaf_found = 1
            else:
                next_node = traversed_tree.RIGHT_SIBLING(next_node)
                leaf_found = 0
        else:
            next_node = traversed_tree.LEFTMOST_CHILD(next_node)

        if next_node == traversed_tree.ROOT():
            break
    print(preorder_listing)
    print(preorder_label_listing)
    return traversed_tree

if __name__ == '__main__':
    test_tree = loctree()
    # test_tree.header = [[], [], [], [1, 2], [], [], [], [], [6, 7], [5, 8], [4, 9], [3, 10]]
    # test_tree.labels = ['NULL', 22, 23, 45, 27, 12, 7, 9, 16, 28, 55, 100]
    # test_tree.root = 11
    node_2 = test_tree.CREATE3(2, test_tree.CREATE0(5), test_tree.CREATE0(6), test_tree.CREATE0(7))
    node_3 = test_tree.CREATE3(3, test_tree.CREATE0(8), test_tree.CREATE0(9), test_tree.CREATE0(10))
    node_4 = test_tree.CREATE3(4, test_tree.CREATE0(11), test_tree.CREATE0(12), test_tree.CREATE0(13))
    node_1 = test_tree.CREATE3(1, node_2, node_3, node_4)
    test_tree = node_1
    preorder(test_tree)