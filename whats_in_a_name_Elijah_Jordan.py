######################################################
# Name: Elijah Jordan                                #
#                                                    #
# Assignment: Construct a set of methods to          #
# manipulate and interrogate an array of characters. #
# Bonus:                                             #
# Log: Sep 29/26                                     #              
# Bugs: None right now                               #
# Sources:Some google for single lines               #
######################################################








name = input ('type your name in this format (First, Middle if applicable, Last,) Must include commas: ') #gathering name for funtctions
def lastname (name): #print last name
    name = name.split(",")   # e.g. "Ann,Lee" -> ["Ann", "Lee"]
    listname = len(name)     # number of name parts

    if listname == 2:
        print (name[1])      # First,Last  last name is the 2nd part
    else:
        print (name[2])      # First,Middle,Last  last name is the 3rd part


def firstname (name):
    """
    Print the first name 
    
    """
    name = name.split(",")
    result = (name[0])

    return result
    


def middlename (name):
    """
    Print the middle name, or a message if there isn't one

    A middle name only works with three parts in the name that was split
    """

    name = name.split(",")
    listname = len(name)

    if listname == 3:
        print (name[1])      # middle name is the 2nd part
    else:
        print ("No middle name supplied ")








def lowercase (name):
    """
    Print the name with every letter in lowercase.
    """
    result = ""
    for char in name:
        if 'A' <= char <= 'Z':
            result = result + chr(ord(char) + 32)
        elif 'a' <= char <= 'z':
                    result = result + chr(ord(char) + 0)
     
        
    return result



def uppercase (name):
    """
    Print the name with every letter in lowercase.
    """
    result = ""
    for char in name:
        if 'a' <= char <= 'z':
            result = result + chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
                            result = result + chr(ord(char) + 0)
    return result


import random   # used b to mix up letters


def randomname (name):
    """
    Print a random name made by mixing up the letters of each name part.


    """
    name = name.split(",")
    listname = len(name)
    count = 0

    # Shuffle the letters inside each part of the name.
    while count < listname:
        letters = list(name[count])       #"Ann" to ["A", "n", "n"]
        random.shuffle(letters)           # mix up 
        name[count] = ''.join(letters)    # back into a string
        count = count + 1

    result = (",".join(name))
    return result


def countvowels (name):
    """
    Count the vowels in the name and return the total

    Also displays a subtotal for each vowel (a, e, i, o, u).
   
    """
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    for char in name: #for how many charachters in name loop to find vowels. 
        if char == 'a' or char == 'A':
            a = a + 1
        elif char == 'e' or char == 'E':
            e = e + 1
        elif char == 'i' or char == 'I':
            i = i + 1
        elif char == 'o' or char == 'O':
            o = o + 1
        elif char == 'u' or char == 'U':
            u = u + 1

    total = a + e + i + o + u
    print ("Vowels: a =", a, " e =", e, " i =", i, " o =", o, " u =", u, " total =", total)
    return total

def reversename (name):
    """
    Reverse the name, display it, and return it

    """
    result = ""
    index = len(name) - 1            # start at the last character

    while index >= 0:
        result = result + name[index]
        index = index - 1

    print ("Reversed:", result)
    return result

def countconsonants (name):
    """
    Return how many consonants are in the name.

    checks if vowel and if a letter if not vowel and letter then its a consnant

    """
    total = 0

    for char in name:
        letter = ('a' <= char <= 'z') or ('A' <= char <= 'Z')   # True if char is a letter
        vowel = char in "aeiouAEIOU"                            # True if char is a vowel

        if letter and not vowel:
            total = total + 1

    return total


def initials (name):
    """
    Return the initials of the name in capitals with periods.
    """
    parts = name.split(",")         # split up name via comma as usual
    result = ""

    for part in parts:
        for char in part:
            if char != " ":                      # first character that isn't a space
                if 'a' <= char <= 'z':
                    char = chr(ord(char) - 32)   # make it a capital, 'a' (97) -> 'A' (65)
                result = result + char + "."
                break                            # only want the first letter of this part

    return result

def hashyphen (name):
    """
    Return true if the Last name contains a hyphen, otherwise its false

    """
    parts = name.split(",")          # split name
    last = parts[len(parts) - 1] #find last part of name
    if last == "" and len(parts) > 1: 
        last = parts[len(parts) - 2] #incase to find last name

    for char in last:
        if char == '-': # if there is a hyphen return true
            return True
    return False

def ispalindrome (name):
    """
    Return True if the first name is a palindrome, if not then false

    In short (detects if reads forwrard and backward same)
    """
    first = name.split(",")[0]       #gets first name because 0 is one
    left = 0                         # index from the front
    right = len(first) - 1           # index from the back

    while left < right: # its just gathering the letter
        front = first[left]
        back = first[right]

        #makes both front and back lowercase everytime
        if 'A' <= front <= 'Z': 
            front = chr(ord(front) + 32)
        if 'A' <= back <= 'Z':
            back = chr(ord(back) + 32)

        if front != back:
            return False
        left = left + 1
        right = right - 1

    return True
def menu (name):
    """
    Show a menu of every function and run the one the user picks.

    
    """
    choice = ""

    while choice != "0":             # keep going until the user quits
        print ()
        print ("========== MENU ==========")
        print ("Current name:", name)
        print (" 1. First name")
        print (" 2. Middle name")
        print (" 3. Last name")
        print (" 4. Lowercase")
        print (" 5. Uppercase")
        print (" 6. Random name")
        print (" 7. Count vowels")
        print (" 8. Reverse name")
        print (" 9. Count consonants")
        print ("10. Initials")
        print ("11. Last name has a hyphen?")
        print ("12. First name is a palindrome?")
        print ("13. Enter a new name")
        print (" 0. Quit")
        choice = input ("Pick an option: ")
        print ()

        if choice == "1":
            print (firstname(name))
        elif choice == "2":
            middlename(name)
        elif choice == "3":
            lastname(name)
        elif choice == "4":
            print ("Lowercase:", lowercase(name))         # returns
        elif choice == "5":
            print ("Uppercase:", uppercase(name))         # returns
        elif choice == "6":
            print(randomname(name))
        elif choice == "7":
            countvowels(name)                             # already prints the subtotals
        elif choice == "8":
            reversename(name)                             # already prints the reversed name
        elif choice == "9":
            print ("Consonants:", countconsonants(name))
        elif choice == "10":
            print ("Initials:", initials(name))
        elif choice == "11":
            print ("Last name has a hyphen:", hashyphen(name))
        elif choice == "12":
            print ("First name is a palindrome:", ispalindrome(name))
        elif choice == "13":
            name = input ('type your name in this format (First, Middle if applicable, Last,) Must include commas')
        elif choice == "0":
            print ("Goodbye")
        else:
            print ("Not an option, pick a number from the menu.")   # anything else typed


menu(name)   # start the menu 

