from pbkdf2 import PBKDF2
from Crypto.Cipher import AES
import os

class PBKDF2_Algorithm():
    salt = os.urandom(8)  # 64-bit salt
    key = PBKDF2("This passphrase is a secret.", salt).read(32)  # 256-bit key
    print(key)
    iv = os.urandom(16)  # 128-bit IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
