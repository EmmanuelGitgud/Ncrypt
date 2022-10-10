#Emmanuel Arabit
#OCT 11 2022
import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

f = Fernet(key)
print(f)

token = f.encrypt(b"hello world")

print (token)

print (f.decrypt(token))


