#!/usr/bin/python3

# Cameron J. Calv
# Assignment 3
# CS260 Data Structures

# Project Problem 2: Closed Hash Table Dictionary Implementation
import string
import random

last_probe_number = 0

def hash(bucket_number, character_string):
    sum = 0
    for character in character_string:
        sum = sum + ord(character)
    hash_value = sum % bucket_number
    return hash_value

class closedHash():

    # Creates a new dictionary defaulted as the NULL dictionary
    # Hash table implementations have a set of buckets with a default of 10
    def __init__(self, number_of_buckets=10):
        self.buckets = number_of_buckets
        self.hashtable = {}
        for bucket in range(self.buckets):
            self.hashtable[bucket] = "NULL"
        return
    # Determines which bucket x would be found in the dictionary
    # Tracks how many probes were performed to find an open bucket via global variable
    # Returns a value equal to bucket number if the dictionary is full
    def locate(self, x):
        initial = hash(self.buckets, x)
        global last_probe_number
        last_probe_number = 0
        index_mod = 0
        while (index_mod < self.buckets) and \
            not (self.hashtable[(initial + index_mod) % self.buckets] == x) and \
            not (self.hashtable[(initial + index_mod) % self.buckets] == "NULL"):
            index_mod = index_mod + 1
        last_probe_number = index_mod + 1
        return ((initial + index_mod) % self.buckets)

    # Does what 'locate' does and also stops at a deleted entry
    # Tracks how many probes were performed to find an open bucket via global variable
    def locate1(self, x):
        initial = hash(self.buckets, x)
        global last_probe_number
        last_probe_number = 0
        index_mod = 0
        while (index_mod < self.buckets) and \
                not (self.hashtable[(initial + index_mod) % self.buckets] == x) and \
                not (self.hashtable[(initial + index_mod) % self.buckets] == "NULL") and \
                not (self.hashtable[(initial + index_mod) % self.buckets] == "DELETED"):
            index_mod = index_mod + 1
        last_probe_number = index_mod + 1
        return ((initial + index_mod) % self.buckets)

    # Inserts a new element x into the dictionary
    # Returns "UNDEF" if the dictionary is full
    def INSERT(self, x):
        if self.hashtable[self.locate(x)] == x:
            return
        bucket = self.locate1(x)
        if (self.hashtable[bucket] == "NULL") or (self.hashtable[bucket] == "DELETED"):
            self.hashtable[bucket] = x
        else:
            return "UNDEF"

    # Deletes the element x from the dictionary and inserts DELETED where the element once was
    # Dictionary remains unchanged if x is not within the dictionary
    def DELETE(self, x):
        bucket = self.locate(x)
        if self.hashtable[bucket] == x:
            self.hashtable[bucket] = "DELETED"
        return

    # Determines whether element x is a member of the dictionary
    # Returns true if x is a member
    # Returns false if x is not a member
    def MEMBER(self, x):
        if self.hashtable[self.locate(x)] == x:
            return 1
        else:
            return 0

    # Makes this dictionary a NULL dictionary
    def MAKENULL(self):
        # Step through the dictionary and make each entry NULL
        for bucket in range(self.buckets):
            self.hashtable[bucket] = "NULL"
        return

if __name__ == '__main__':
    print("Let's create a test dictionary!")
    test_dict = closedHash()
    print("Adding a few things to the dictionary...")
    test_dict.INSERT("Apple")
    test_dict.INSERT("Banana")
    test_dict.INSERT("Carrot")
    test_dict.INSERT("Durian")
    test_dict.INSERT("Eggplant")
    test_dict.INSERT("Flowers")
    print("Element insertion finished!")
    print("Testing to make sure each element is present in the dictionary...")
    assert (test_dict.MEMBER("Apple") == 1)
    assert (test_dict.MEMBER("Banana") == 1)
    assert (test_dict.MEMBER("Carrot") == 1)
    assert (test_dict.MEMBER("Durian") == 1)
    assert (test_dict.MEMBER("Eggplant") == 1)
    assert (test_dict.MEMBER("Flowers") == 1)
    print("Element presence test passed!")
    print("Deleting a few elements from the dictionary...")
    test_dict.DELETE("Durian")
    test_dict.DELETE("Carrot")
    test_dict.DELETE("Eggplant")
    test_dict.DELETE("Flowers")
    # Attempt to delete an element that doesn't exist
    test_dict.DELETE("Gator Ade")
    print("Element deletion finished!")
    print("Attempt to make add more than the dictionary can handle...")
    test_dict.INSERT("One")
    test_dict.INSERT("Two")
    test_dict.INSERT("Three")
    test_dict.INSERT("Four")
    test_dict.INSERT("Five")
    test_dict.INSERT("Six")
    test_dict.INSERT("Seven")
    test_dict.INSERT("Eight")
    # Insert a final element beyond the max of the dictionary
    assert (test_dict.INSERT("Nine") == "UNDEF")
    assert (test_dict.MEMBER("Nine") == 0)
    print("Overflow test passed!")
    print("Testing to make sure the elements have been successfully deleted...")
    assert (test_dict.MEMBER("Carrot") == 0)
    assert (test_dict.MEMBER("Durian") == 0)
    assert (test_dict.MEMBER("Eggplant") == 0)
    assert (test_dict.MEMBER("Flowers") == 0)
    print("Element deletion test passed!")
    print("Setting the dictionary back to NULL...")
    test_dict.MAKENULL()
    print("Testing for presence of remaining elements...")
    assert (test_dict.MEMBER("Apple") == 0)
    assert (test_dict.MEMBER("Banana") == 0)
    print("Null test passed!")
    print("All dictionary tests completed!")

    print("Beginning timing tests for insertion and deletion up to n = 7000...\n\n")
    test_dict = closedHash(7000)
    header_string = "[Number of Elements]\t[Insert Probes]\t[Delete Probes]\t[Insert Expected]\t[Delete Expected]"
    print(header_string)
    number_of_trials = 5000
    letters = string.ascii_lowercase
    insert_probes = []
    delete_probes = []
    expected_probe_insert = []
    expected_probe_delete = []
    max_word_length = 15
    for i in range(number_of_trials):
        insert_expect_value = 0.5*(1+1/((1-i/test_dict.buckets)**2))
        expected_probe_insert.append(insert_expect_value)
        delete_expect_value = 0.5*(1+1/(1-i/test_dict.buckets))
        expected_probe_delete.append(delete_expect_value)
        random_word = ''.join(random.sample(letters, random.randint(1, max_word_length)))

        test_dict.INSERT(random_word)
        constant_insert = last_probe_number
        test_dict.DELETE(random_word)
        constant_delete = last_probe_number

        test_dict.INSERT(random_word)

        insert_probes.append(constant_insert)
        delete_probes.append(constant_delete)

        statement = str(i) + "\t" + str(constant_insert) + "\t" + str(constant_delete) + "\t" + str(insert_expect_value) + "\t" + str(delete_expect_value)
        print(statement)

    print("\n\nAverage expected for insertion: " + str(sum(expected_probe_insert) / len(expected_probe_insert)))
    print("Average constant for insertion: " + str(sum(insert_probes) / len(insert_probes)))
    print("\n\nAverage expected for deletion: " + str(sum(expected_probe_delete) / len(expected_probe_delete)))
    print("Average constant for deletion: " + str(sum(delete_probes) / len(delete_probes)))