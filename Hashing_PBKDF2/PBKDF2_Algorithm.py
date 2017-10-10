from passlib.hash import pbkdf2_sha256
import pickle
import os



class PBKDF2_Algorithm():

    def generate_Salt(self): #generate an 8-bit salt for hashing password
        return os.urandom(8)

    def generate_Hash(self,username,inputPassword):
        salt = PBKDF2_Algorithm.generate_Salt(object) #calling within the same class require class name.def
        hash=pbkdf2_sha256.encrypt(inputPassword,rounds=10000,salt=salt) #with raw password, iterate it with salt 10000 times to avoid brute force and dictionary attack or rainbow attack
        PBKDF2_Algorithm.storing_Salt_Hash(object,username,salt,hash) #store username,salt,hash, BUT NOT RAW PASSWORD

    def storing_Salt_Hash(self, username, salt, hash):
        try: #try if the file exist or not
            with open('../Hashing_PBKDF2/Admin_Login.pickle','rb') as readFile:  # load pickle file and load it into variable 'temp'
                temp = pickle.load(readFile)
                temp[username] = [salt, hash]  # add a new entry for specific user with specific salt and hash
            with open('../Hashing_PBKDF2/Admin_Login.pickle', 'wb') as writeFile:
                pickle.dump(temp, writeFile, protocol=pickle.HIGHEST_PROTOCOL) # write it to file
        except IOError: #if the file doesnt exist
            with open('../Hashing_PBKDF2/Admin_Login.pickle', 'wb') as writeFile: #empty file
                temp={} #empty dict to store first input value
                temp[username]=[salt,hash]
                pickle.dump(temp, writeFile, protocol=pickle.HIGHEST_PROTOCOL) #write to file

    def check_Password(self,username,password): #return a true or false value indicating passsword valid or not
        with open('../Hashing_PBKDF2/Admin_Login.pickle', 'rb') as readFile:
            passwordList = pickle.load(readFile) #fetch all the dict entry from file
            try:
                return (pbkdf2_sha256.verify(password,passwordList[username][1])) # get the user input password (login) and check it with the hash from that user's dict, python will keep track which algorithm u use and how many iteration you used.
            except KeyError:
                print("key not found")
                return False
