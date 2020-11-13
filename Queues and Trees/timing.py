#!/usr/bin/python3

# Cameron J. Calv
# Assignment 2
# CS260 Data Structures

# Project Problem 3: PreOrder and PostOrder Timing
import time

from loctree import loctree
from lcrstree import lcrstree


# Accepts a tree as a parameter and returns the pre-order of the tree's labels
# Assumes that the tree is not the Null tree
def preorder(traversed_tree):
    # Traverse through the tree and add each node traversed the first time it is accessed
    current_traversal_path = []
    preorder_listing = []
    preorder_label_listing = []
    leaf_found = 0
    next_node = traversed_tree.ROOT()
    while 1:
        node_label = traversed_tree.LABEL(next_node)
        current_traversal_path.append(next_node)
        if next_node not in preorder_listing:
            # If we have never accessed this node before
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
    return preorder_label_listing


# Accepts a tree as a parameter and returns the post-order of the tree's labels
# Assumes that the tree is not the Null tree
def postorder(traversed_tree):
    # Traverse through the tree and add each node traversed the second time it is accessed
    current_traversal_path = []
    postorder_listing = []
    postorder_label_listing = []
    leaf_found = 0
    next_node = traversed_tree.ROOT()
    while 1:
        node_label = traversed_tree.LABEL(next_node)
        current_traversal_path.append(next_node)
        if (traversed_tree.LEFTMOST_CHILD(next_node) == 0):
            leaf_found = 1
        # If a leaf has been found or a parent has no more leaves to access
        if leaf_found:
            postorder_listing.append(next_node)
            postorder_label_listing.append(node_label)
            if traversed_tree.RIGHT_SIBLING(next_node) == 0:
                next_node = traversed_tree.PARENT(next_node)
                leaf_found = 1
            else:
                next_node = traversed_tree.RIGHT_SIBLING(next_node)
                leaf_found = 0
        else:
            next_node = traversed_tree.LEFTMOST_CHILD(next_node)
        if next_node == traversed_tree.ROOT():
            # If the root node has been reached at the end
            postorder_listing.append(next_node)
            postorder_label_listing.append(traversed_tree.LABEL(next_node))
            break
    return postorder_label_listing


if __name__ == '__main__':
    null_loc = loctree()
    null_lcrs = lcrstree()
    # Initialize a full order 3-tree of height 3 using the LOC and LCRS implementations
    n = 3
    level_1 = [1]
    level_2 = [x for x in range(2, 5)]
    level_3 = [x for x in range(5, 14)]
    level_3_nodes_loc = []
    level_3_nodes_lcrs = []
    for index in level_3:
        level_3_nodes_loc.append(null_loc.CREATE0(index))
        level_3_nodes_lcrs.append(null_lcrs.CREATE0(index))
    level_2_nodes_loc = []
    level_2_nodes_lcrs = []
    node_index = 0
    for index in level_2:
        level_2_nodes_loc.append(null_loc.CREATE3(index,
                                                  level_3_nodes_loc[node_index],
                                                  level_3_nodes_loc[node_index + 1],
                                                  level_3_nodes_loc[node_index + 2]))
        level_2_nodes_lcrs.append(null_lcrs.CREATE3(index,
                                                    level_3_nodes_lcrs[node_index],
                                                    level_3_nodes_lcrs[node_index + 1],
                                                    level_3_nodes_lcrs[node_index + 2]))
        node_index = node_index + 3
    loc_height_3 = null_loc.CREATE3(level_1[0],
                                    level_2_nodes_loc[0],
                                    level_2_nodes_loc[1],
                                    level_2_nodes_loc[2])
    lcrs_height_3 = null_lcrs.CREATE3(level_1[0],
                                      level_2_nodes_lcrs[0],
                                      level_2_nodes_lcrs[1],
                                      level_2_nodes_lcrs[2])
    # Initialize a full order 3-tree of height 4 using the LOC and LCRS implementations
    n = 4
    level_4 = [x for x in range(14, 41)]
    level_4_nodes_loc = []
    level_4_nodes_lcrs = []
    for index in level_4:
        level_4_nodes_loc.append(null_loc.CREATE0(index))
        level_4_nodes_lcrs.append(null_lcrs.CREATE0(index))
    level_3_nodes_loc = []
    level_3_nodes_lcrs = []
    node_index = 0
    for index in level_3:
        level_3_nodes_loc.append(null_loc.CREATE3(index,
                                                  level_4_nodes_loc[node_index],
                                                  level_4_nodes_loc[node_index + 1],
                                                  level_4_nodes_loc[node_index + 2]))
        level_3_nodes_lcrs.append(null_lcrs.CREATE3(index,
                                                    level_4_nodes_lcrs[node_index],
                                                    level_4_nodes_lcrs[node_index + 1],
                                                    level_4_nodes_lcrs[node_index + 2]))
        node_index = node_index + 3
    level_2_nodes_loc = []
    level_2_nodes_lcrs = []
    node_index = 0
    for index in level_2:
        level_2_nodes_loc.append(null_loc.CREATE3(index,
                                                  level_3_nodes_loc[node_index],
                                                  level_3_nodes_loc[node_index + 1],
                                                  level_3_nodes_loc[node_index + 2]))
        level_2_nodes_lcrs.append(null_lcrs.CREATE3(index,
                                                    level_3_nodes_lcrs[node_index],
                                                    level_3_nodes_lcrs[node_index + 1],
                                                    level_3_nodes_lcrs[node_index + 2]))
        node_index = node_index + 3
    loc_height_4 = null_loc.CREATE3(level_1[0],
                                    level_2_nodes_loc[0],
                                    level_2_nodes_loc[1],
                                    level_2_nodes_loc[2])
    lcrs_height_4 = null_lcrs.CREATE3(level_1[0],
                                      level_2_nodes_lcrs[0],
                                      level_2_nodes_lcrs[1],
                                      level_2_nodes_lcrs[2])

    # Begin time trials
    header_string = "[Height]\t[LOC Time (sec)]\t[LCRS Time (sec)]\n"
    print("Starting program for Pre-Order.")
    print(header_string)
    # Pre-Order of height 3
    start = time.perf_counter()
    preorder_list = preorder(loc_height_3)
    stop = time.perf_counter()
    loc_time = stop - start

    start = time.perf_counter()
    preorder_list = preorder(lcrs_height_3)
    stop = time.perf_counter()
    lcrs_time = stop - start

    preorder_statement = str(3) + "\t" + str(loc_time) + "\t" + str(lcrs_time)
    print(preorder_statement, "\tPre-Order Traversal")

    # Pre-Order of height 4
    start = time.perf_counter()
    preorder(loc_height_4)
    stop = time.perf_counter()
    loc_time = stop - start

    start = time.perf_counter()
    preorder(lcrs_height_4)
    stop = time.perf_counter()
    lcrs_time = stop - start

    preorder_statement = str(4) + "\t" + str(loc_time) + "\t" + str(lcrs_time)
    print(preorder_statement, "\tPre-Order Traversal")
    print("\n\n")
    print("Starting program for Pre-Order.")
    print(header_string)
    # Post-Order of height 3
    start = time.perf_counter()
    postorder(loc_height_3)
    stop = time.perf_counter()
    loc_time = stop - start

    start = time.perf_counter()
    postorder(lcrs_height_3)
    stop = time.perf_counter()
    lcrs_time = stop - start

    postorder_statement = str(3) + "\t" + str(loc_time) + "\t" + str(lcrs_time)
    print(postorder_statement, "\tPost-Order Traversal")

    # Post-Order of height 4
    start = time.perf_counter()
    postorder(loc_height_4)
    stop = time.perf_counter()
    loc_time = stop - start

    start = time.perf_counter()
    postorder(lcrs_height_4)
    stop = time.perf_counter()
    lcrs_time = stop - start

    postorder_statement = str(4) + "\t" + str(loc_time) + "\t" + str(lcrs_time)
    print(postorder_statement, "\tPost-Order Traversal")