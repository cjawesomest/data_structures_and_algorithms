#!/usr/bin/python3

# Cameron J. Calv
# Assignment 2
# CS260 Data Structures

# Project Problem 2: List of Children Tree Implementation

class loctree():

    # Creates a NULL TREE
    def __init__(self):
        self.header = [[]]
        self.labels = ["NULL"]
        self.root = 0

    # Returns the parent of node n in the tree.
    # Returns NULL Node 0 if n is the root node
    def PARENT(self, n):
        for p in range(1, len(self.header)):
            children = self.header[p]
            for child in children:
                if child == n:
                    return (p)
        return (0)

    # Returns the leftmost child of node n
    # Returns NULL Node 0 if n is a leaf  and has no children
    def LEFTMOST_CHILD(self, n):
        children = self.header[n]
        if not children:
            return 0
        else:
            return children[0]

    # Returns the right sibling of node n
    # Returns "NULL" if n is the rightmost child and has no right sibling
    def RIGHT_SIBLING(self, n):
        parent = self.PARENT(n)
        siblings = self.header[parent]
        found_self = 0
        for sibling in siblings:
            if sibling == n:
                found_self = 1
                continue
            if found_self:
                return sibling
        return 0

    # Returns the label of node n
    def LABEL(self, n):
        return self.labels[n]

    # Creates a new node with label v
    def CREATE0(self, v):
        # Create a null tree and add one node with label v
        new_tree = loctree()
        new_tree.header.append([])
        new_tree.labels.append(v)
        new_tree.root = 1
        return new_tree

    # Creates a new node with label v and gives it one child which is
    # the root of the supplied tree parameter
    def CREATE1(self, v, T1):
        # Create a copy of T1 and add a new node v with its only child the root of T1
        new_tree = loctree()
        new_tree.header = T1.header.copy()
        new_tree.labels = T1.labels.copy()
        new_tree.header.append([T1.ROOT()])
        new_tree.labels.append(v)
        new_tree.root = len(new_tree.header) - 1
        return new_tree

    # Creates a new node with label v and gives it two children which are
    # the roots of the supplied tree parameters in order from left to right
    def CREATE2(self, v, T1, T2):
        # Create a copy of T1 as a temporary tree
        temp_tree = loctree()
        temp_tree.header = T1.header.copy()
        temp_tree.labels = T1.labels.copy()
        temp_tree.root = T1.root
        # Add new nodes to the temporary tree corresponding to the tree structure of T2
        for node in T2.header[1:len(T2.header)]:
            new_child_indices = []
            for child in node:
                new_child_indices.append(child + len(T1.header) - 1)
            temp_tree.header.append(new_child_indices)
        for label in T2.labels[1:len(T2.labels)]:
            temp_tree.labels.append(label)
        T2_new_root = T2.ROOT() + len(T1.header) - 1
        new_tree = self.CREATE1(v, temp_tree)
        new_tree.header[-1].append(T2_new_root)
        return new_tree

    # Creates a new node with label v and gives it three children which are
    # the roots of the supplied tree parameters in order from left to right
    def CREATE3(self, v, T1, T2, T3):
        # Create a copy of T1 as a temporary tree
        temp_tree = loctree()
        temp_tree.header = T1.header.copy()
        temp_tree.labels = T1.labels.copy()
        temp_tree.root = T1.root
        # Add new nodes to the temporary tree corresponding to the tree structure of T2
        for node in T2.header[1:len(T2.header)]:
            new_child_indices = []
            for child in node:
                new_child_indices.append(child + len(T1.header) - 1)
            temp_tree.header.append(new_child_indices)
        for label in T2.labels[1:len(T2.labels)]:
            temp_tree.labels.append(label)
        T2_new_root = T2.ROOT() + len(T1.header) - 1
        # Create a copy of the temporary tree as a second temporary tree and do as before for T3
        temp_tree_2 = loctree()
        temp_tree_2.header = temp_tree.header.copy()
        temp_tree_2.labels = temp_tree.labels.copy()
        temp_tree_2.root = temp_tree.root
        for node in T3.header[1:len(T3.header)]:
            new_child_indices = []
            for child in node:
                new_child_indices.append(child + len(temp_tree.header) - 1)
            temp_tree_2.header.append(new_child_indices)
        for label in T3.labels[1:len(T3.labels)]:
            temp_tree_2.labels.append(label)
        T3_new_root = T3.ROOT() + len(temp_tree.header) - 1
        new_tree = self.CREATE1(v, temp_tree_2)
        new_tree.header[-1].append(T2_new_root)
        new_tree.header[-1].append(T3_new_root)
        return new_tree

    # Returns the root node of the tree
    # Returns "NULL" if this is the NULL TREE
    def ROOT(self):
        return self.root

    # Makes this tree the NULL TREE
    def MAKENULL(self):
        temp = loctree()
        self.header = temp.header.copy()
        self.labels = temp.labels.copy()
        self.root = 0
        return


if __name__ == '__main__':
    print("Let's create a test tree! With root A with children B and C.")
    print("B has child D and C has children E, F, and G")
    print("Creating tree...")
    null_tree = loctree()
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
