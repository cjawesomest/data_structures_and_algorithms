#!/usr/bin/python3

# Cameron J. Calv
# CS260 Data Structures
# Assignment 1
class arrayStack():
    # Stack is initialized with a maximum length parameter defaulted to 100
    # If no array is provided, an empty stack is created
    def __init__(self, array=[], maxlength=100):
        self.maxlength = maxlength
        self.elements = ["Undef" for i in range(self.maxlength)]
        self.top = self.maxlength + 0
        if array:
            for i in range(len(array)):
                self.elements[i] = array[i]
                self.top = self.top - 1

    # Takes a stack as a parameter and returns the element at the top of the stack
    # Returns undefined if the stack is empty
    def TOP(self):
        if self.EMPTY():
            return "Undef"
        else:
            return self.elements[self.top]

    # Takes a stack as a parameter and returns the element at the top of the stack
    # Top element of stack is deleted after being returned
    # Returns undefined if the stack is empty
    def POP(self):
        if self.EMPTY():
            return "Undef"
        else:
            self.top = self.top + 1
            return

    # Takes a stack as a parameter and pushes the given element to the top of the stack
    # Returns undefined if the stack is full
    def PUSH(self, element):
        if self.top == 1:
            return "Undef"
        else:
            self.top = self.top - 1
            self.elements[self.top] = element
        return

    # Takes a stack as a parameter and empties the stack of its contents
    # Returns a boolean value indicated whether the operation was successful or not
    def EMPTY(self):
        if self.top >= self.maxlength:
            return 1
        else:
            return 0

    # Takes a stack as a parameter and sets it equal to the null stack
    def MAKENULL(self):
        self.top = self.maxlength + 0
        return

    # Prints a string representation of the stack to view its contents
    def PRINTSTACK(self):
        if not self.EMPTY():
            string = "{BOTTOM} ["
            count = self.maxlength - 1
            while count > self.top - 1:
                string = string + str(self.elements[count]) + ", "
                count = count - 1
            string = string + "\b\b] {TOP}"
        else:
            string = "{BOTTOM} [ NULL ] {TOP}"
        print(string)
        return string


if __name__ == '__main__':
    #Initialize the stack
    test_stack = arrayStack()
    test_stack.PUSH("A")
    test_stack.PUSH("B")
    test_stack.PUSH("C")
    test_stack.PUSH("D")
    test_stack.PUSH("E")
    test_stack.PUSH("F")
    test_stack.PRINTSTACK()
    #Testing essential stack operations
    print("What element is at the top of our stack? " + test_stack.TOP())
    test_stack.POP()
    print("If we pop our stack, now what's at the top? " + test_stack.TOP())
    print("Let's push the letter 'Q' to the top of the stack!")
    test_stack.PUSH("Q")
    test_stack.PRINTSTACK()
    if (test_stack.EMPTY()):
        print("Is our stack empty? Yes!")
    else:
        print("Is our stack empty? No!")
    print("Let's make our stack Null!")
    test_stack.MAKENULL()
    if (test_stack.EMPTY()):
        print("Is it empty now? Yes!")
    else:
        print("Is it empty now? No!")
    test_stack.PRINTSTACK()
    print("What's at the top of the stack now? " + str(test_stack.TOP()))
    print("What if we Pop? What happens? " + str(test_stack.POP()))
    print("Can we add to a Null stack?")
    test_stack.PUSH("Of Course We Can!")
    test_stack.PRINTSTACK()
