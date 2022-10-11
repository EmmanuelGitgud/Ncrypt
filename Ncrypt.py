#Emmanuel Arabit
#OCT 11 2022

from cryptography.fernet import Fernet

#import key
with open('key.json','rb') as f:
    key = f.read()
key = Fernet(key)

#open file
file = 'topsecret.zip'
w_file = file.split('.')
w_file = w_file[0]

with open(file, 'rb') as f:
    data = f.read()

#encrypt file
token = key.encrypt(data)

# save file
with open(w_file + '.crypt', 'wb') as f:
    f.write(token)



