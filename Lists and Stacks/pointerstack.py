#!/usr/bin/python3

# Cameron J. Calv
# CS260 Data Structures
# Assignment 1
class space():
    # Initializes a space which is as described on page 48 of the textbook
    # Used to create cursors which allow for the use of pointer implementations in Python
    def __init__(self, maxlength):
        self.first = 0
        self.element = ["Undef" for i in range(maxlength)]
        self.next = ["Undef" for i in range(maxlength)]

class pointerStack():
    # Stack is initialized with a maximum length parameter defaulted to 100
    # If no array is provided, an empty stack is created
    def __init__(self, array = [], maxlength = 100):
        self.maxlength = maxlength
        self.pointerspace = space(self.maxlength)
        for i in range(self.maxlength - 1):
            if i == 0:
                self.pointerspace.element[i] = "Head"
                self.pointerspace.first = i
                self.pointerspace.next[i] = i + 1
            elif i == len(array) + 1:
                self.pointerspace.element[i] = "NULL"
                self.pointerspace.next[i] = "NULL"
                break
            else:
                self.pointerspace.element[i] = array[i-1]
                self.pointerspace.next[i] = i+1

    # Takes a stack as a parameter and returns the element at the top of the stack
    # Returns undefined if the stack is empty
    def TOP(self):
        top = self.pointerspace.element[self.pointerspace.next[self.pointerspace.first]]
        if top == "NULL":
            return "Undef"
        else:
            return top

    # Takes a stack as a parameter and returns the element at the top of the stack
    # Top element of stack is deleted after being returned
    # Returns undefined if the stack is empty
    def POP(self):
        if self.EMPTY():
            return "Undef"
        else:
            self.pointerspace.next[self.pointerspace.first] = \
                self.pointerspace.next[self.pointerspace.next[self.pointerspace.first]]
            return

    # Takes a stack as a parameter and pushes the given element to the top of the stack
    # Returns undefined if the stack is full
    def PUSH(self, element):
        for i in range(self.maxlength):
            cell = self.pointerspace.element[i]
            next = self.pointerspace.next[i]
            if cell == "Undef" and next == "Undef":
                self.pointerspace.element[i] = element
                self.pointerspace.next[i] = self.pointerspace.next[self.pointerspace.first]
                self.pointerspace.next[self.pointerspace.first] = i
                return

    # Takes a stack as a parameter and empties the stack of its contents
    # Returns a boolean value indicated whether the operation was successful or not
    def EMPTY(self):
        if self.TOP() == "Undef":
            return 1
        else:
            return 0

    # Takes a stack as a parameter and sets it equal to the null stack
    def MAKENULL(self):
        self.pointerspace.next[self.pointerspace.first] = 1
        return

    # Prints a string representation of the stack to view its contents
    def PRINTSTACK(self):
        if not self.EMPTY():
            string = "{TOP} ["
            current = self.pointerspace.first
            while current != "NULL":
                next = self.pointerspace.next[current]
                current_element = self.pointerspace.element[current]
                if current_element != "Undef" and current_element != "NULL" and current_element != "Head":
                    string = string + current_element + ", "
                current = next
            string = string + "\b\b] {BOTTOM}"
        else:
            string = "{TOP} [ NULL ] {BOTTOM}"
        print(string)
        return string

if __name__ == '__main__':
    # Initialize the stack
    test_stack = pointerStack()
    test_stack.PUSH("A")
    test_stack.PUSH("B")
    test_stack.PUSH("C")
    test_stack.PUSH("D")
    test_stack.PUSH("E")
    test_stack.PUSH("F")
    test_stack.PRINTSTACK()
    # Testing essential stack operations
    print("What element is at the top of our stack? "+test_stack.TOP())
    test_stack.POP()
    print("If we pop our stack, now what's at the top? "+test_stack.TOP())
    print("Let's push the letter 'Q' to the top of the stack!")
    test_stack.PUSH("Q")
    test_stack.PRINTSTACK()
    if (test_stack.EMPTY()):
        print("Is our stack empty? Yes!")
    else:
        print("Is our stack empty? No!")
    print("Let's make our stack Null!")
    test_stack.MAKENULL()
    if(test_stack.EMPTY()):
        print("Is it empty now? Yes!")
    else:
        print("Is it empty now? No!")
    test_stack.PRINTSTACK()
    print("What's at the top of the stack now? " + str(test_stack.TOP()))
    print("What if we Pop? What happens? "+str(test_stack.POP()))
    print("Can we add to a Null stack?")
    test_stack.PUSH("Of Course We Can!")
    test_stack.PRINTSTACK()
