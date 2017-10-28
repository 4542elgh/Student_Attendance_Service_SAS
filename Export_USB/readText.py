class readText:

#%B6048880000876543^ PERSON/TWO BOB ^4912120000000000000000000000000?;6048880000419099=4912120303451234?

    sText = input("Please swipe your ID card: ")

    def deCode(sText):
    #check if scanned properly
        if(len(sText) < 66):
            print("Rescan your ID card please")

    print(len(sText))

    split = sText.split('^')
    forwardSlash = split[1].find('/')
    splitThird = split[2]
    #print(split)

    name = split[1]

    firstName = split[0][forwardSlash+1:len()]
    lastName = name[0:forwardSlash]
    cin = splitThird[len(splitThird)-10:len(splitThird)-1]
