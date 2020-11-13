#!/usr/bin/python3

# Cameron J. Calv
# Assignment 3
# CS260 Data Structures

# Project Problem 1: Open Hash Table Dictionary Implementation
import string
import random


# Creates a hash value based on a given character string
# Hash value depends on the number of buckets in the dictionary hash tables
def hash(bucket_number, character_string):
    sum = 0
    for character in character_string:
        sum = sum + ord(character)
    hash_value = sum % bucket_number
    return hash_value


class openHash():

    # Creates a new dictionary defaulted as the NULL dictionary
    # Hash table implementations have a set of buckets with a default of 10
    def __init__(self, number_of_buckets=100):
        self.buckets = number_of_buckets
        self.hashtable = {}
        for bucket in range(self.buckets):
            self.hashtable[bucket] = ["NULL"]
        return

    # Inserts a new element x into the dictionary
    # Returns "UNDEF" if the dictionary is full
    # Returns number of probes to insert element x otherwise
    def INSERT(self, x):
        # Add x if it is not already present
        probes = 0
        if not self.MEMBER(x):
            probes = 1
            self.hashtable[hash(self.buckets, x)].append(x)
            probes = probes + len(self.hashtable[hash(self.buckets, x)])
        return probes

    # Deletes the element x from the dictionary
    # Dictionary remains unchanged if x is not within the dictionary
    # Returns number of probes to delete element x
    def DELETE(self, x):
        # Retrieve the bucket that x would be a part of
        bucket = hash(self.buckets, x)
        probes = 1
        index = 0
        # Step through the bucket and delete the element x if it is found
        for element in self.hashtable[bucket]:
            probes = probes + 1
            if element == x:
                del self.hashtable[bucket][index]
                return probes
            index = index + 1
        return probes

    # Determines whether element x is a member of the dictionary
    # Returns true if x is a member
    # Returns false if x is not a member
    def MEMBER(self, x):
        # Retrieve the bucket that x would be a part of
        current = self.hashtable[hash(self.buckets, x)]
        # Step through the bucket and see if x is present
        for element in current:
            if element == x:
                return 1
        return 0

    # Makes this dictionary a NULL dictionary
    def MAKENULL(self):
        # Step through the dictionary and make each entry NULL
        for bucket in range(self.buckets):
            self.hashtable[bucket] = ["NULL"]
        return


if __name__ == '__main__':
    print("Let's create a test dictionary!")
    test_dict = openHash()
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

    print("Beginning timing tests for insertion and deletion up to n = 50000...\n\n")
    header_string = "[Number of Elements]\t[Insert Probes]\t[Delete Probes]\t[1+N/B]"
    print(header_string)
    number_of_trials = 50000
    letters = string.ascii_lowercase
    insert_probes = []
    delete_probes = []
    expected_probes = []
    max_word_length = 15
    for i in range(number_of_trials+1):
        one_plus_n_over_b = 1 + (i/test_dict.buckets)
        expected_probes.append(one_plus_n_over_b)
        random_word = ''.join(random.sample(letters, random.randint(1, max_word_length)))

        constant_insert = test_dict.INSERT(random_word)
        constant_delete = test_dict.DELETE(random_word)

        test_dict.INSERT(random_word)

        insert_probes.append(constant_insert)
        delete_probes.append(constant_delete)

        statement = str(i) + "\t" + str(constant_insert) + "\t" + str(constant_delete) + "\t" + str(one_plus_n_over_b)
        print(statement)

    print("\n\nAverage 1 + N/B: " + str(sum(expected_probes) / len(expected_probes)))
    print("Average constant for insertion: " + str(sum(insert_probes) / len(insert_probes)))
    print("Average constant for deletion: " + str(sum(delete_probes) / len(delete_probes)))
