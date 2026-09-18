name = input ('type your name in this format (First, Middle if applicable, Last,) Must include commas')


def reverse (name):
    length = len(name)-1
    output = ''



    while length >= 0:
        output = output + name[length]
        length = length - 1 
    
    print (output)

def lastname (name):
    name = name.split(",")
    listname = len(name)

    if listname == 2:
        print (name[1])
    else:
        print (name[2])
   
    



def firstname (name):
    name = name.split(",")
    print (name[0])
    

def middlename (name):
    name = name.split(",")
    listname = len(name)
    
    if listname == 3:
        print (name[1])
    else
        print ("No middle name supplied")
   
    

lastname(name)