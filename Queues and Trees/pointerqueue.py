#!/usr/bin/python3

# Cameron J. Calv
# Assignment 2
# CS260 Data Structures

# Project Problem 1: Pointer Queue Implementation

# Cellspace structure to use as references for elements in the queue
class cellspace():
    # Create unpopulated cellspace with a single NULL pointer
    def __init__(self, maxsize=100):
        self.next = [0 for zero in range(maxsize)]
        self.element = ["UNDEF" for zero in range(maxsize)]
        self.element[0] = "NULL"

class pointerQueue():

    # Initializes the queue as Null
    def __init__(self):
        self.cellspace = cellspace()
        self.front = 0
        self.rear = 0

    # Makes the queue the NULL queue
    def MAKENULL(self):
        self.front = 0
        self.rear = self.front

    # Returns a boolean stating whether or not this queue is empty
    def EMPTY(self):
        if self.front == self.rear:
            return 1
        else:
            return 0

    # Returns the first element on the queue
    # Returns "NULL" if the queue is empty
    def FRONT(self):
        if self.EMPTY():
            return "NULL"
        else:
            return self.cellspace.element[self.cellspace.next[self.front]]

    # Inserts element x at the end of the queue
    def ENQUEUE(self, x):
        index = 0
        for element in self.cellspace.element:
            # Found a free space in memory
            if element == "UNDEF":
                break
            index = index + 1
        self.cellspace.next[self.rear] = index
        self.rear = index
        self.cellspace.element[self.rear] = x
        self.cellspace.next[self.rear] = 0


    # Deletes the first element of the queue
    # Returns "NULL" if the queue is empty
    def DEQUEUE(self):
        if self.EMPTY():
            return "NULL"
        else:
            self.front = self.cellspace.next[self.front]

if __name__ == '__main__':
    print("Let's create a test queue...")
    test_queue = pointerQueue()
    print("Test queue created!")
    print("Let's add a few elements to our queue...")
    test_queue.ENQUEUE('A')
    test_queue.ENQUEUE('B')
    test_queue.ENQUEUE('C')
    test_queue.ENQUEUE('D')
    test_queue.ENQUEUE('E')
    test_queue.ENQUEUE('F')
    print("Making sure that the first element in is at the front of the queue...")
    assert (test_queue.FRONT() == 'A')
    print("First element test passed!")
    print("Let's step through the queue and print back out what was placed inside.")
    print(test_queue.FRONT())
    test_queue.DEQUEUE()
    assert (test_queue.FRONT() == 'B')
    print(test_queue.FRONT())
    test_queue.DEQUEUE()
    assert (test_queue.FRONT() == 'C')
    print(test_queue.FRONT())
    test_queue.DEQUEUE()
    assert (test_queue.FRONT() == 'D')
    print(test_queue.FRONT())
    test_queue.DEQUEUE()
    assert (test_queue.FRONT() == 'E')
    print(test_queue.FRONT())
    test_queue.DEQUEUE()
    assert (test_queue.FRONT() == 'F')
    print(test_queue.FRONT())
    test_queue.DEQUEUE()
    print("Now let's make sure our queue is empty.")
    assert(test_queue.EMPTY() == 1)
    print("If we add a few more elements and then create a NULL queue, are we left with an empty queue?")
    test_queue.ENQUEUE('N')
    test_queue.ENQUEUE('U')
    test_queue.ENQUEUE('L')
    test_queue.ENQUEUE('L')
    test_queue.MAKENULL()
    assert(test_queue.EMPTY() == 1)
    print("All tests passed!")