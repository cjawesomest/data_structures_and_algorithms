#!/usr/bin/python3

# Cameron J. Calv
# CS260 Data Structures
# Assignment 1
import random
import time
from arraylist import *
from arraystack import *
from pointerlist import *
from pointerstack import *
from os.path import join

if __name__ == '__main__':
    #Stack timing
    max_n = 2400
    write_to_file = 1
    print_to_console = 0
    print_to_console_at_all = 0
    header_string = "[Size]\t[Array Time (sec)]\t[Pointer Time (sec)]\t[Library Time (sec)]\n"
    save_path = "."
    if print_to_console:
        print("Starting program for stack implementations.")
        print(header_string)
    if write_to_file:
        push_file = open(join(save_path, "stack_push.txt"), "w+")
        push_file.write(header_string)
        pop_file = open(join(save_path, "stack_pop.txt"), "w+")
        pop_file.write(header_string)

    for i in range(1, max_n + 1):
        if print_to_console_at_all:
            print(str(i) + "...")
        a_stack = arrayStack([], i * 100)
        p_stack = pointerStack([], i * 100)
        l_stack = []
        for j in range(i):
            random_element = random.randint(0, 100)
            a_stack.PUSH(random_element)
            p_stack.PUSH(random_element)
            l_stack.append(random_element)
        random_element = random.randint(0, 100)

        # Iterated Insertion Push
        start = time.perf_counter()
        a_stack.PUSH(random_element)
        stop = time.perf_counter()
        a_time = stop - start

        start = time.perf_counter()
        p_stack.PUSH(random_element)
        stop = time.perf_counter()
        p_time = stop - start

        start = time.perf_counter()
        l_stack.append(random_element)
        stop = time.perf_counter()
        l_time = stop - start
        push_statement = str(i) + "\t" + str(a_time) + "\t" + str(p_time) + "\t" + str(l_time)
        if print_to_console:
            print(push_statement, "\tInsertion (Pushing)")
        if write_to_file:
            push_file.write(push_statement + "\n")

            # Iterated Deletion Pop
        start = time.perf_counter()
        a_stack.POP()
        stop = time.perf_counter()
        a_time = stop - start

        start = time.perf_counter()
        p_stack.POP()
        stop = time.perf_counter()
        p_time = stop - start

        start = time.perf_counter()
        l_stack.pop(i)
        stop = time.perf_counter()
        l_time = stop - start
        pop_statement = str(i) + "\t" + str(a_time) + "\t" + str(p_time) + "\t" + str(l_time)
        if print_to_console:
            print(pop_statement, "\tDeletion (Popping)")
        if write_to_file:
            pop_file.write(pop_statement + "\n")

    if write_to_file:
        push_file.close()
        pop_file.close()
    if print_to_console: print("Completed")






    # List timing
    max_n = 2400
    write_to_file = 1
    print_to_console = 0
    print_to_console_at_all = 0
    header_string = "[Size]\t[Array Time (sec)]\t[Pointer Time (sec)]\t[Library Time (sec)]\n"
    save_path = "."
    if print_to_console:
        print("Starting program for list implementations.")
        print(header_string)
    if write_to_file:
        insertion_front_file = open(join(save_path, "list_insert_front.txt"), "w+")
        insertion_front_file.write(header_string)
        insertion_back_file = open(join(save_path, "list_insert_back.txt"), "w+")
        insertion_back_file.write(header_string)
        deletion_front_file = open(join(save_path, "list_deletion_front.txt"), "w+")
        deletion_front_file.write(header_string)
        deletion_back_file = open(join(save_path, "list_deletion_back.txt"), "w+")
        deletion_back_file.write(header_string)
        traversal_file = open(join(save_path, "list_traversal.txt"), "w+")
        traversal_file.write(header_string)

    for i in range(1, max_n + 1):
        if print_to_console_at_all:
            print(str(i) + "...")
        a_list = arrayList([], i * 100)
        p_list = pointerList([], i * 100)
        l_list = []
        for j in range(i):
            random_element = random.randint(0, 100)
            a_list.INSERT(random_element, j + 1)
            p_list.INSERT(random_element, j + 1)
            l_list.append(random_element)
        random_element = random.randint(0, 100)

        # Iterated Insertion at Front
        start = time.perf_counter()
        a_list.INSERT(random_element, 1)
        stop = time.perf_counter()
        a_time = stop - start

        start = time.perf_counter()
        p_list.INSERT(random_element, 1)
        stop = time.perf_counter()
        p_time = stop - start

        start = time.perf_counter()
        l_list.insert(1, random_element)
        stop = time.perf_counter()
        l_time = stop - start
        insert_front_statement = str(i) + "\t" + str(a_time) + "\t" + str(p_time) + "\t" + str(l_time)
        if print_to_console:
            print(insert_front_statement, "\tInsertion at Front")
        if write_to_file:
            insertion_front_file.write(insert_front_statement + "\n")

        # Iterated Deletion at Front
        start = time.perf_counter()
        a_list.DELETE(1)
        stop = time.perf_counter()
        a_time = stop - start

        start = time.perf_counter()
        p_list.DELETE(1)
        stop = time.perf_counter()
        p_time = stop - start

        start = time.perf_counter()
        del l_list[1]
        stop = time.perf_counter()
        l_time = stop - start
        delete_front_statement = str(i) + "\t" + str(a_time) + "\t" + str(p_time) + "\t" + str(l_time)
        if print_to_console:
            print(delete_front_statement, "\tDeletion at Front")
        if write_to_file:
            deletion_front_file.write(delete_front_statement + "\n")

        # Iterated Insertion at Back
        start = time.perf_counter()
        a_list.INSERT(random_element, i + 1)
        stop = time.perf_counter()
        a_time = stop - start

        start = time.perf_counter()
        p_list.INSERT(random_element, i + 1)
        stop = time.perf_counter()
        p_time = stop - start

        start = time.perf_counter()
        l_list.insert(i, random_element)
        stop = time.perf_counter()
        l_time = stop - start
        insert_back_statement = str(i) + "\t" + str(a_time) + "\t" + str(p_time) + "\t" + str(l_time)
        if print_to_console:
            print(insert_back_statement, "\tInsertion at Back")
        if write_to_file:
            insertion_back_file.write(insert_back_statement + "\n")

        # Iterated Deletion at Back
        start = time.perf_counter()
        a_list.DELETE(i + 1)
        stop = time.perf_counter()
        a_time = stop - start

        start = time.perf_counter()
        p_list.DELETE(i + 1)
        stop = time.perf_counter()
        p_time = stop - start

        start = time.perf_counter()
        del l_list[i]
        stop = time.perf_counter()
        l_time = stop - start
        delete_back_statement = str(i) + "\t" + str(a_time) + "\t" + str(p_time) + "\t" + str(l_time)
        if print_to_console:
            print(delete_back_statement, "\tDeletion at Back")
        if write_to_file:
            deletion_back_file.write(delete_back_statement + "\n")

        # Traversal
        start = time.perf_counter()
        for j in range(1, i + 1):
            a_list.RETRIEVE(j)
        stop = time.perf_counter()
        a_time = stop - start

        start = time.perf_counter()
        for j in range(1, i + 1):
            p_list.RETRIEVE(j)
        stop = time.perf_counter()
        p_time = stop - start

        start = time.perf_counter()
        for j in range(0, i):
            l_list[i - 1]
        stop = time.perf_counter()
        l_time = stop - start
        traversal_statement = str(i) + "\t" + str(a_time) + "\t" + str(p_time) + "\t" + str(l_time)
        if print_to_console:
            print(traversal_statement, "\tTraversal")
        if write_to_file:
            traversal_file.write(traversal_statement + "\n")

    if write_to_file:
        insertion_front_file.close()
        insertion_back_file.close()
        deletion_front_file.close()
        deletion_back_file.close()
        traversal_file.close()

