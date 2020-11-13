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

class pointerList():
    # Initializes a space which is as described on page 48 of the textbook
    # Used to create cursors which allow for the use of pointer implementations in Python
    def __init__(self, array = [], maxlength=100):
        self.maxlength = maxlength
        self.last = len(array)
        self.pointerspace = space(self.maxlength)
        for i in range(self.END()+1):
            if i == 0:
                self.pointerspace.element[i] = "Head"
                self.pointerspace.first = i
                self.pointerspace.next[i] = i + 1
            elif i == self.END():
                self.pointerspace.element[i] = "NULL"
                self.pointerspace.next[i] = "NULL"
            else:
                self.pointerspace.element[i] = array[i-1]
                self.pointerspace.next[i] = i+1

    # Takes a list as a parameter and returns the position of the first element
    # If the list is empty, the END of the list is returned
    def FIRST(self):
        if self.last != 0:
            return self.pointerspace.first
        else:
            return self.END()

    # Takes a list as a parameter and returns the position of the last element of the list
    def END(self):
        return self.last + 1

    # Takes a list and a position as parameters and returns the element found at the given position
    # Returns undefined if the position is not present in the list
    def RETRIEVE(self, position):
        count = 0
        current = self.pointerspace.first
        if position < self.END() and position >= self.FIRST():
            while count != position:
                current = self.pointerspace.next[current]
                count = count + 1
            return self.pointerspace.element[current]
        else:
             return "Undef"

    # Takes a list and an element as a parameter and returns the position of the element to be located in the list
    # Returns the END of the list if the element is not found
    def LOCATE(self, element):
        count = 0
        current = self.pointerspace.first
        while current != "NULL":
            if self.pointerspace.element[current] == element:
                return count
            current = self.pointerspace.next[current]
            count = count + 1
        return self.END()

    # Takes a list and a position as parameters and returns the position of the element after the position provided
    # Returns END if the last position is specified and undefined if the END position is supplied
    def NEXT(self, position):
        return self.pointerspace.next[position]

    # Takes a list and a position as parameters and returns the position of the element before the position provided
    # Returns undefined if the first position is specified and the last position if the END is specified
    def PREVIOUS(self, position):
        current = self.pointerspace.first
        previous = "Undef"
        while current != position:
            previous = current
            current = self.pointerspace.next[current]
        return previous

    # Takes a list and an element and a position as parameters and inserts the element at the position in the list
    # If the position does not exist, the list remains unchanged
    def INSERT(self, new_element, position):
        #Find open memory for new element in list
        if position >= 0 and position <= self.END():
            for i in range(self.maxlength):
                cell = self.pointerspace.element[i]
                next = self.pointerspace.next[i]
                if cell == "Undef" and next == "Undef":
                    self.pointerspace.element[i] = new_element
                    current = self.pointerspace.first
                    before = -1
                    for j in range(len(self.pointerspace.next)):
                        if j == position:
                            self.pointerspace.next[i] = current
                            self.pointerspace.next[before] = i
                            break
                        before = current
                        current = self.pointerspace.next[current]
                    self.last = self.last+1
                    return
        else:
            return "Undef"

    # Take a list and a position as a parameter and deletes that position in the list if it exists
    # Returns undefined if the position is invalid
    def DELETE(self, position):
        count = 0
        if position >= 0 and position <= self.END():
            current = self.pointerspace.first
            while count != position-1:
                next = self.pointerspace.next[current]
                current = next
                count = count + 1
            next = self.pointerspace.next[current]
            self.pointerspace.next[current] = self.pointerspace.next[self.pointerspace.next[current]]
            self.pointerspace.next[next] = "Undef"
            self.pointerspace.element[next] = "Undef"
            self.last = self.last - 1
        else:
            return "Undef"

    # Takes a list as a parameter and sets if equal to the null list
    def MAKENULL(self):
        self.pointerspace.first = self.END()
        self.last = self.END()
        return

    # Takes a list as a parameter and returns its contents in a string representation
    def PRINTLIST(self):
        string = "["
        current = self.pointerspace.first
        while current != "NULL":
            next = self.pointerspace.next[current]
            current_element = self.pointerspace.element[current]
            if current_element != "Undef" and current_element != "NULL" and current_element != "Head":
                string = string + str(current_element)+", "
            current = next
        string = string+"\b\b]"
        if self.pointerspace.first == self.last:
            print("[ NULL ]")
        else:
            print(string)
        return

if __name__ == '__main__':
    # Initialize the list
    test_list = pointerList()
    test_list.INSERT("Birds", 1)
    test_list.INSERT("Planes", 2)
    test_list.INSERT("Automobiles", 3)
    test_list.INSERT("Fish", 4)
    test_list.INSERT("Dinosaurs", 5)
    test_list.PRINTLIST()
    # Test valid list operations
    print("First Element at Position : " + str(test_list.FIRST()))
    print("First Element is : " + str(test_list.RETRIEVE(test_list.FIRST())))
    print("Last Element at Position : " + str(test_list.END() - 1))
    print("Last Element is : " + str(test_list.RETRIEVE(test_list.END() - 1)))
    print("End of List is at Position : " + str(test_list.END()))
    print("End of List contains : " + str(test_list.RETRIEVE(test_list.END())))
    print("Where is 'Fish' in the list? : Position " + str(test_list.LOCATE("Fish")))
    print("What about 'Racecars'? : Position " + str(test_list.LOCATE("Racecars")))
    if (test_list.LOCATE(4) == test_list.END()):
        print("Is that in the list? : No")
    else:
        print("Is that in the list? : Yes")
    print("What comes after Position 10? : Position " + str(test_list.NEXT(10)))
    print("What comes after Position 3? : Position " + str(test_list.NEXT(3)))
    print("What comes before the first position? : Position " + str(test_list.PREVIOUS(test_list.FIRST())))
    print("What comes before the END? : Position " + str(test_list.PREVIOUS(test_list.END())))
    if (test_list.PREVIOUS(test_list.END()) == test_list.last):
        print("Is this the last position? : Yes")
    else:
        print("Is this the last position? : No")
    print("Let's insertk. 'Animals' at Position 2")
    test_list.INSERT('Animals', 2)
    test_list.PRINTLIST()
    print("Let's delete what's at Position 3")
    test_list.DELETE(3)
    test_list.PRINTLIST()
    print("Now, let's nullify our structure.")
    test_list.MAKENULL()
    test_list.PRINTLIST()
    print("All gone!")
