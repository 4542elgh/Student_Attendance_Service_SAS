

import re
def paste_string():
    string = input("Please swipe the card")

    split = string.split("^")

    name = split[1]

    # Split the slash inside the card reader
    forward_slash = split[1].find('/')
    # Get first name from the name
    first_name = name[forward_slash + 1:len(name)]
    # Get last name from the name
    last_name = name[0:forward_slash]
    three = split[2]
    cin = three[len(three) - 10:len(three) - 1]


    # Print out the first name, last name, and CIN number

    print("First Name: " + first_name + " Last Name: " + last_name + " CIN: " + cin)


paste_string()