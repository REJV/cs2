name = input ('type your name in this format (First, Middle if applicable, Last,) Must include commas') #gathering name for funtctions
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
    string = Full name as "First,Last" or "First,Middle,Last"
    name = name.split(",")
    print (name[0])
    """


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


# Show the user's last name.
lastname(name)
firstname(name)
middlename(name)


def initails (name):
    """
IN PROGRESS

    """
    name = name.split(",")
    listname = len(name)

    if listname == 3:
        print (name[1])
    else:
        print ("")




def lowercase (name):
    """
    Print the name with every letter in lowercase.
    """
    print (name.lower())



def uppercase (name):
    """
    Print the name with every letter in uppercase.
    """

    print (name.upper())

lowercase(name)
uppercase(name)
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

    print (",".join(name))

randomname(name)