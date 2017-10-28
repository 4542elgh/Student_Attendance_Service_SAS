

import re
def paste_string():
    string = input("Please swipe the card")

    split = string.split("^")

    name = split[1]

    forward_slash = split[1].find('/')
    first_name = name[forward_slash + 1:len(name)]
    last_name = name[0:forward_slash]
    three = split[2]
    cin = three[len(three) - 10:len(three) - 1]
    print("First Name: " + first_name + " Last Name: " + last_name + " CIN: " + cin)


paste_string()