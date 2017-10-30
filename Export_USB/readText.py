class ReadText:

    #%B6048880000876543^ PERSON/TWO BOB ^4912120000000000000000000000000?;6048880000419099=4912120303451234?
    def decode(self):
        string = input("Enter something: ")

        split = string.split('^')

        print(split)
        name = split[1]
        forward_slash = split[1].find('/')
        first_name = name[forward_slash + 1:len(name)]
        last_name = name[0:forward_slash]
        three = split[2]
        cin = three[len(three) - 10:len(three) - 1]
        print("First name: " + first_name + " Last name: " + last_name + " CIN: " + cin)

    decode()
    input()
