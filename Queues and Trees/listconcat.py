#!/usr/bin/python3

# Cameron J. Calv
# Assignment 2
# CS260 Data Structures

# Project Problem 5: Textbook Problem 2.4

from arraylist import arrayList


# Function to concatenate a list of lists
def listconcat(list_of_lists):
    # Start with a Null list
    concatenated_list = arrayList([])
    index = 1
    outer_first = list_of_lists.FIRST()
    outer_last = list_of_lists.END()
    # Step through each element in the list of lists
    for outer_element_index in range(outer_first, outer_last):
        outer_element = list_of_lists.RETRIEVE(outer_element_index)
        inner_first = outer_element.FIRST()
        inner_last = outer_element.END()
        # Step through each element of each list in the list of lists
        for inner_element_index in range(inner_first, inner_last):
            # Retrieve that element and insert it into the concatenated list
            inner_element = outer_element.RETRIEVE(inner_element_index)
            concatenated_list.INSERT(inner_element, index)
            index = index + 1
    return concatenated_list


if __name__ == '__main__':
    print(
        "Let's fill our test list up with four lists \n[[A, B], [C], [D, E, F, G], [H, I]]")
    test_list = arrayList()
    list_1 = arrayList(["A", "B"])
    list_2 = arrayList(["C"])
    list_3 = arrayList(["D", "E", "F", "G"])
    list_4 = arrayList(["H", "I"])
    test_list.INSERT(list_1, 1)
    test_list.INSERT(list_2, 2)
    test_list.INSERT(list_3, 3)
    test_list.INSERT(list_4, 4)
    print("Testing for list structure validity...")
    assert (test_list.RETRIEVE(1) == list_1)
    assert (test_list.RETRIEVE(2) == list_2)
    assert (test_list.RETRIEVE(3) == list_3)
    assert (test_list.RETRIEVE(4) == list_4)
    print("Structure validity confirmed!")
    print("Concatenating the list of lists...")
    concat_list = listconcat(test_list)
    print("Confirming successful concatenation...")
    assert (concat_list.RETRIEVE(1) == "A")
    assert (concat_list.RETRIEVE(2) == "B")
    assert (concat_list.RETRIEVE(3) == "C")
    assert (concat_list.RETRIEVE(4) == "D")
    assert (concat_list.RETRIEVE(5) == "E")
    assert (concat_list.RETRIEVE(6) == "F")
    assert (concat_list.RETRIEVE(7) == "G")
    assert (concat_list.RETRIEVE(8) == "H")
    assert (concat_list.RETRIEVE(9) == "I")
    print("Concatenation confirmed!")
    concat_list.PRINTLIST()
