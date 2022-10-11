#Emmanuel Arabit
#OCT 11 2022

from cryptography.fernet import Fernet

#import key
with open('key.json','rb') as f:
    key = f.read()
key = Fernet(key)

#open file
file = 'topsecret.jpg'
with open(file, 'rb') as f:
    data = f.read()

#encrypt file
token = key.encrypt(data)

#save file
with open('encrypted.jpg', 'wb') as f:
    f.write(token)


