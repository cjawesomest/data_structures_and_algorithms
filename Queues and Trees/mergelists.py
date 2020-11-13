#!/usr/bin/python3

# Cameron J. Calv
# Assignment 2
# CS260 Data Structures

# Project Problem 4: Textbook Problem 2.3b

from arraylist import arrayList
from listconcat import listconcat


def mergelists(*lists):
    # Compile all lists supplied into a composite list
    c_index = 0
    composite_list = arrayList([])
    for list in lists:
        c_index = c_index + 1
        composite_list.INSERT(list, c_index)
    # Add composite list elements in a sorted fashion
    m_index = 1
    merged_list = listconcat(composite_list)
    final_length = merged_list.END() - merged_list.FIRST()
    merged_sorted_list = arrayList([])
    while (merged_sorted_list.END() - merged_sorted_list.FIRST() != final_length):
        current_min_index = 1
        current_min = merged_list.RETRIEVE(current_min_index)
        for index in range(merged_list.FIRST(), merged_list.END()):
            element = merged_list.RETRIEVE(index)
            if element < current_min:
                current_min = element
                current_min_index = index
        merged_sorted_list.INSERT(current_min, m_index)
        m_index = m_index + 1
        merged_list.DELETE(current_min_index)
    return merged_sorted_list


if __name__ == '__main__':
    print("Let's start off initializing a few lists.")
    print("[A, D, E]")
    list_1 = arrayList(["A", "D", "E"])
    print("[B, F, I]")
    list_2 = arrayList(["B", "F", "I"])
    print("[C, K, L]")
    list_3 = arrayList(["C", "K", "L"])
    print("[G, H, J, M, N, O]")
    list_4 = arrayList(["G", "H", "J", "M", "N", "O"])
    print("Merging all sorted lists...")
    test_m_list = mergelists(list_1, list_2, list_3, list_4)
    print("Lists merged!")
    print("Confirming sorted structure of merged list...")
    py_sortable_list = []
    for i in range(1, test_m_list.END()):
        py_sortable_list.append(test_m_list.RETRIEVE(i))
    sorted_list = py_sortable_list.copy()
    sorted_list.sort()
    assert(sorted_list == py_sortable_list)
    print("Sorted structure test passed!")
    print("Confirming that all lists were merged properly...")
    array_of_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "M", "N", "O"]
    for letter in array_of_letters:
        assert (test_m_list.LOCATE(letter) > 0)
    print("All list elements present!")