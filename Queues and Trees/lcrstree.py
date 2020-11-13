#!/usr/bin/python3

# Cameron J. Calv
# Assignment 2
# CS260 Data Structures

# Project Problem 2: Leftmost-Child Rightmost-Sibling Tree Implementation

# Cellspace structure to use as references for nodes
class cellspace():
    # Create unpopulated cellspace with a single NULL pointer
    def __init__(self, maxsize=100):
        self.leftmost_child = [0 for zero in range(maxsize)]
        self.label = ["UNDEF" for zero in range(maxsize)]
        self.label[0] = "NULL"
        self.right_sibling = [0 for zero in range(maxsize)]


class lcrstree():

    # Creates a NULL TREE
    def __init__(self):
        self.cellspace = cellspace()
        self.root = 0
        return

    # Returns the parent of node n in the tree.
    # Returns NULL Node 0 if n is the root node
    def PARENT(self, n):
        node = 0
        # Check if n is a leftmost child
        for child in self.cellspace.leftmost_child:
            if child == n:
                return node
            node = node + 1
        node = 0
        for potential_parent in self.cellspace.label:
            child = self.cellspace.leftmost_child[node]
            if child != 0:
                sibling = self.cellspace.right_sibling[child]
                while sibling != 0:
                    if sibling == n:
                        return node
                    else:
                        sibling = self.cellspace.right_sibling[sibling]
            node = node + 1
        return 0

    # Returns the leftmost child of node n
    # Returns NULL Node 0 if n is a leaf  and has no children
    def LEFTMOST_CHILD(self, n):
        return self.cellspace.leftmost_child[n]

    # Returns the right sibling of node n
    # Returns "NULL" if n is the rightmost child and has no right sibling
    def RIGHT_SIBLING(self, n):
        return self.cellspace.right_sibling[n]

    # Returns the label of node n
    def LABEL(self, n):
        return self.cellspace.label[n]

    # Creates a new node with label v
    def CREATE0(self, v):
        new_tree = lcrstree()
        # new_tree.cellspace.leftmost_child = self.cellspace.leftmost_child.copy()
        # new_tree.cellspace.right_sibling = self.cellspace.right_sibling.copy()
        # new_tree.cellspace.label = self.cellspace.label.copy()
        index = 0
        # Find open space in cellspace to store the new node
        for label in new_tree.cellspace.label:
            if label == "UNDEF":
                break
            index = index + 1
        new_tree.cellspace.label[index] = v
        new_tree.root = index
        return new_tree

    # Creates a new node with label v and gives it one child which is
    # the root of the supplied tree parameter
    def CREATE1(self, v, T1):
        new_tree = lcrstree()
        new_tree.cellspace.leftmost_child = T1.cellspace.leftmost_child.copy()
        new_tree.cellspace.right_sibling = T1.cellspace.right_sibling.copy()
        new_tree.cellspace.label = T1.cellspace.label.copy()
        index = 0
        for label in new_tree.cellspace.label:
            if label == "UNDEF":
                break
            index = index + 1
        new_tree.cellspace.label[index] = v
        new_tree.cellspace.leftmost_child[index] = T1.root
        new_tree.root = index
        return new_tree

    # Creates a new node with label v and gives it two children which are
    # the roots of the supplied tree parameters in order from left to right
    def CREATE2(self, v, T1, T2):
        new_tree = lcrstree()
        new_tree_root = 0
        for label in new_tree.cellspace.label:
            if label == "UNDEF":
                break
            new_tree_root = new_tree_root + 1
        new_tree.cellspace.label[new_tree_root] = v
        new_tree.cellspace.right_sibling[new_tree_root] = 0
        # Add the contents of T1 to the cell space of the new tree
        T1_new_root = new_tree_root + T1.ROOT()
        nodes_in_T1 = 0
        for index in range(len(T1.cellspace.label)):
            T1_current_label = T1.cellspace.label[index]
            T1_current_lc = T1.cellspace.leftmost_child[index]
            T1_current_rs = T1.cellspace.right_sibling[index]
            if T1_current_label == "UNDEF":
                break
            elif T1_current_label != "NULL":
                next_new_index = nodes_in_T1 + new_tree_root + 1
                nodes_in_T1 = nodes_in_T1 + 1
                new_tree.cellspace.label[next_new_index] = T1_current_label
                if T1_current_lc != 0:
                    new_tree.cellspace.leftmost_child[next_new_index] = new_tree_root + T1_current_lc
                if T1_current_rs != 0:
                    new_tree.cellspace.right_sibling[next_new_index] = new_tree_root + T1_current_rs
        new_tree.cellspace.leftmost_child[new_tree_root] = T1_new_root
        # Add the contents of T2 to the cell space of the new tree
        T2_new_root = nodes_in_T1 + new_tree_root + 1
        nodes_in_T2 = 0
        for index in range(len(T2.cellspace.label)):
            T2_current_label = T2.cellspace.label[index]
            T2_current_lc = T2.cellspace.leftmost_child[index]
            T2_current_rs = T2.cellspace.right_sibling[index]
            if T2_current_label == "UNDEF":
                break
            elif T2_current_label != "NULL":
                next_new_index = nodes_in_T2 + T2_new_root
                nodes_in_T2 = nodes_in_T2 + 1
                new_tree.cellspace.label[next_new_index] = T2_current_label
                if T2_current_lc != 0:
                    new_tree.cellspace.leftmost_child[next_new_index] = new_tree_root + nodes_in_T1 + T2_current_lc
                if T2_current_rs != 0:
                    new_tree.cellspace.right_sibling[next_new_index] = new_tree_root + nodes_in_T1 + T2_current_rs
        new_tree.cellspace.leftmost_child[new_tree_root] = T1_new_root
        new_tree.cellspace.right_sibling[T1_new_root] = T2_new_root
        new_tree.cellspace.right_sibling[T2_new_root] = 0
        new_tree.root = new_tree_root
        return new_tree

    # Creates a new node with label v and gives it three children which are
    # the roots of the supplied tree parameters in order from left to right
    def CREATE3(self, v, T1, T2, T3):
        new_tree = lcrstree()
        new_tree_root = 0
        for label in new_tree.cellspace.label:
            if label == "UNDEF":
                break
            new_tree_root = new_tree_root + 1
        new_tree.cellspace.label[new_tree_root] = v
        new_tree.cellspace.right_sibling[new_tree_root] = 0
        # Add the contents of T1 to the cell space of the new tree
        T1_new_root = new_tree_root + T1.ROOT()
        nodes_in_T1 = 0
        for index in range(len(T1.cellspace.label)):
            T1_current_label = T1.cellspace.label[index]
            T1_current_lc = T1.cellspace.leftmost_child[index]
            T1_current_rs = T1.cellspace.right_sibling[index]
            if T1_current_label == "UNDEF":
                break
            elif T1_current_label != "NULL":
                next_new_index = nodes_in_T1 + new_tree_root + 1
                nodes_in_T1 = nodes_in_T1 + 1
                new_tree.cellspace.label[next_new_index] = T1_current_label
                if T1_current_lc != 0:
                    new_tree.cellspace.leftmost_child[next_new_index] = new_tree_root + T1_current_lc
                if T1_current_rs != 0:
                    new_tree.cellspace.right_sibling[next_new_index] = new_tree_root + T1_current_rs
        new_tree.cellspace.leftmost_child[new_tree_root] = T1_new_root
        # Add the contents of T2 to the cell space of the new tree
        T2_new_root = nodes_in_T1 + new_tree_root + 1
        nodes_in_T2 = 0
        for index in range(len(T2.cellspace.label)):
            T2_current_label = T2.cellspace.label[index]
            T2_current_lc = T2.cellspace.leftmost_child[index]
            T2_current_rs = T2.cellspace.right_sibling[index]
            if T2_current_label == "UNDEF":
                break
            elif T2_current_label != "NULL":
                next_new_index = nodes_in_T2 + T2_new_root
                nodes_in_T2 = nodes_in_T2 + 1
                new_tree.cellspace.label[next_new_index] = T2_current_label
                if T2_current_lc != 0:
                    new_tree.cellspace.leftmost_child[next_new_index] = new_tree_root + nodes_in_T1 + T2_current_lc
                if T2_current_rs != 0:
                    new_tree.cellspace.right_sibling[next_new_index] = new_tree_root + nodes_in_T1 + T2_current_rs
        # Add the contents of T3 to the cell space of the new tree
        T3_new_root = nodes_in_T1 + nodes_in_T2 + new_tree_root + 1
        nodes_in_T3 = 0
        for index in range(len(T3.cellspace.label)):
            T3_current_label = T3.cellspace.label[index]
            T3_current_lc = T3.cellspace.leftmost_child[index]
            T3_current_rs = T3.cellspace.right_sibling[index]
            if T3_current_label == "UNDEF":
                break
            elif T3_current_label != "NULL":
                next_new_index = nodes_in_T3 + T3_new_root
                nodes_in_T3 = nodes_in_T3 + 1
                new_tree.cellspace.label[next_new_index] = T3_current_label
                if T3_current_lc != 0:
                    new_tree.cellspace.leftmost_child[
                        next_new_index] = new_tree_root + nodes_in_T1 + nodes_in_T2 + T3_current_lc
                if T3_current_rs != 0:
                    new_tree.cellspace.right_sibling[
                        next_new_index] = new_tree_root + nodes_in_T1 + nodes_in_T2 + T3_current_rs
        new_tree.cellspace.leftmost_child[new_tree_root] = T1_new_root
        new_tree.cellspace.right_sibling[T1_new_root] = T2_new_root
        new_tree.cellspace.right_sibling[T2_new_root] = T3_new_root
        new_tree.cellspace.right_sibling[T3_new_root] = 0
        new_tree.root = new_tree_root
        return new_tree

    # Returns the root node of the tree
    # Returns "NULL" if this is the NULL TREE
    def ROOT(self):
        return self.root

    # Makes this tree the NULL TREE
    def MAKENULL(self):
        self.cellspace = cellspace()
        self.root = 0
        return


if __name__ == '__main__':
    print("Let's create a test tree! With root A with children B and C.")
    print("B has child D and C has children E, F, and G")
    print("Creating tree...")
    null_tree = lcrstree()
    node_e = null_tree.CREATE0("E")
    node_f = null_tree.CREATE0("F")
    node_g = null_tree.CREATE0("G")
    node_c = null_tree.CREATE3("C", node_e, node_f, node_g)
    node_d = null_tree.CREATE0("D")
    node_b = null_tree.CREATE1("B", node_d)
    test_tree = null_tree.CREATE2("A", node_b, node_c)
    tree_root_a = test_tree.ROOT()
    print("Test Tree created!")

    # Confirm structure of the tree
    print("Confirming tree structure...")
    assert (test_tree.LABEL(tree_root_a) == "A")
    tree_node_b = test_tree.LEFTMOST_CHILD(tree_root_a)
    assert (test_tree.LABEL(tree_node_b) == "B")
    tree_node_c = test_tree.RIGHT_SIBLING(tree_node_b)
    assert (test_tree.LABEL(tree_node_c) == "C")
    tree_node_d = test_tree.LEFTMOST_CHILD(tree_node_b)
    assert (test_tree.LABEL(tree_node_d) == "D")
    tree_node_e = test_tree.LEFTMOST_CHILD(tree_node_c)
    assert (test_tree.LABEL(tree_node_e) == "E")
    tree_node_f = test_tree.RIGHT_SIBLING(tree_node_e)
    assert (test_tree.LABEL(tree_node_f) == "F")
    tree_node_g = test_tree.RIGHT_SIBLING(tree_node_f)
    assert (test_tree.LABEL(tree_node_g) == "G")
    print("Tree structure test passed!")

    # Null test node G for children and right siblings
    print("Testing for node G children and siblings...")
    tree_node_g_sibling = test_tree.RIGHT_SIBLING(tree_node_g)
    assert (test_tree.LABEL(tree_node_g_sibling) == "NULL")
    tree_node_g_child = test_tree.LEFTMOST_CHILD(tree_node_g)
    assert (test_tree.LABEL(tree_node_g_child) == "NULL")
    print("Children and sibling Null testing passed!")

    # Parent testing
    print("Testing for tree parents...")
    tree_node_f_parent = test_tree.PARENT(tree_node_f)
    assert (test_tree.LABEL(tree_node_f_parent) == "C")
    tree_node_c_parent = test_tree.PARENT(tree_node_c)
    assert (test_tree.LABEL(tree_node_c_parent) == "A")
    tree_root_a_parent = test_tree.PARENT(tree_root_a)
    assert (test_tree.LABEL(tree_root_a_parent) == "NULL")
    print("Parent testing passed!")

    # Set tree back to NULL
    print("Setting tree to NULL...")
    test_tree.MAKENULL()
    null_test_tree_root = test_tree.ROOT()
    assert (null_test_tree_root == 0)
    assert (test_tree.LEFTMOST_CHILD(null_test_tree_root) == 0)
    assert (test_tree.RIGHT_SIBLING(null_test_tree_root) == 0)
    assert (test_tree.PARENT(null_test_tree_root) == 0)
    print("NULL tree test passed!")
    print("\nTree structure confirmed!")
