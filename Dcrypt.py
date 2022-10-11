from cryptography.fernet import Fernet

with open('key.json','rb') as f:
    key = f.read()
key = Fernet(key)

file = 'topsecret.crypt'
w_file = file.split('.')
w_file = w_file[0]

with open(file, 'rb') as f:
    data = f.read()

decrypted = key.decrypt(data)

with open (w_file + '.zip', 'wb') as f:
    f.write(decrypted)