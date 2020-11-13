#!/usr/bin/python3

# Cameron J. Calv
# CS260 Data Structures
# Assignment 1

class arrayList():
    # List is initialized with a maximum length parameter defaulted to 100
    # If no array is provided, an empty list is created
    def __init__(self, array = [], maxlength = 100):
        self.maxlength = maxlength
        self.elements = array
        self.last = len(array)
        for i in range(self.maxlength):
            if i >= self.last:
                self.elements.append('Undef')

    # Takes a list as a parameter and returns the position of the first element
    # If the list is empty, the END of the list is returned
    def FIRST(self):
        if self.last != 0:
            return 1
        else:
            return self.END()

    # Takes a list as a parameter and returns the position of the last element of the list
    def END(self):
        return self.last + 1

    # Takes a list and a position as parameters and returns the element found at the given position
    # Returns undefined if the position is not present in the list
    def RETRIEVE(self, position):
        if position < self.END() and position >= self.FIRST():
            return self.elements[position - 1]
        else:
            return 'Undef'

    # Takes a list and an element as a parameter and returns the position of the element to be located in the list
    # Returns the END of the list if the element is not found
    def LOCATE(self, element):
        for i in range(self.END()):
            if self.elements[i] == element:
                return i+1
        return self.END()

    # Takes a list and a position as parameters and returns the position of the element after the position provided
    # Returns END if the last position is specified and undefined if the END position is supplied
    def NEXT(self, position):
        if position == self.last:
            return self.END()
        elif position >= self.END():
            return "Undef"
        elif position < self.last and position >= self.FIRST():
            return position+1
        else:
            return

    # Takes a list and a position as parameters and returns the position of the element before the position provided
    # Returns undefined if the first position is specified and the last position if the END is specified
    def PREVIOUS(self, position):
        if position <= self.FIRST():
            return "Undef"
        elif position == self.END():
            return self.last
        elif position > self.FIRST() and position < self.END():
            return position-1

    # Takes a list and an element and a position as parameters and inserts the element at the position in the list
    # If the position does not exist, the list remains unchanged
    def INSERT(self, element, position):
        for i in reversed(range(self.END())):
            if i >= position-1:
                if i+1 < self.maxlength:
                    self.elements[i+1] = self.RETRIEVE(i+1)
            if i+1 == position:
                self.elements[i] = element
                break
        self.last = self.last+1
        return

    # Take a list and a position as a parameter and deletes that position in the list if it exists
    # Returns undefined if the position is invalid
    def DELETE(self, position):
        if self.RETRIEVE(position) == "Undef" or position == self.END():
            return "Undef"
        for i in range(self.last):
            if i+1 >= position:
                if i < self.maxlength:
                    self.elements[i] = self.RETRIEVE(i+2)
        self.last = self.last-1
        return

    # Takes a list as a parameter and sets if equal to the null list
    def MAKENULL(self):
        self.last = 0
        return

    # Takes a list as a parameter and returns its contents in a string representation
    def PRINTLIST(self):
        string = "["
        for i in range(self.END()):
            if i == 0:
                continue
            elif i == self.last:
                string = string + str(self.RETRIEVE(i))
            else:
                string = string+str(self.RETRIEVE(i))+", "
        string = string+"]"
        print(string)
        return


if __name__ == '__main__':
    #Initialize the list
    test_list = arrayList()
    test_list.INSERT("Birds", 1)
    test_list.INSERT("Planes", 2)
    test_list.INSERT("Automobiles", 3)
    test_list.INSERT("Fish", 4)
    test_list.INSERT("Dinosaurs", 5)
    test_list.PRINTLIST()
    #Test valid list operations
    print("First Element at Position : "+str(test_list.FIRST()))
    print("First Element is : "+str(test_list.RETRIEVE(test_list.FIRST())))
    print("Last Element at Position : "+str(test_list.END()-1))
    print("Last Element is : "+str(test_list.RETRIEVE(test_list.END()-1)))
    print("End of List is at Position : "+str(test_list.END()))
    print("End of List contains : "+str(test_list.RETRIEVE(test_list.END())))
    print("Where is 'Fish' in the list? : Position "+str(test_list.LOCATE("Fish")))
    print("What about 'Racecars'? : Position "+str(test_list.LOCATE("Racecars")))
    if (test_list.LOCATE(4) == test_list.END()):
        print("Is that in the list? : No")
    else:
        print("Is that in the list? : Yes")
    print("What comes after Position 10? : Position "+str(test_list.NEXT(10)))
    print("What comes after Position 3? : Position "+str(test_list.NEXT(3)))
    print("What comes before the first position? : Position "+str(test_list.PREVIOUS(test_list.FIRST())))
    print("What comes before the END? : Position "+str(test_list.PREVIOUS(test_list.END())))
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



