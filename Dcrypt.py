from cryptography.fernet import Fernet

with open('key.json','rb') as f:
    key = f.read()
key = Fernet(key)

file = 'encrypted.jpg'
with open(file, 'rb') as f:
    data = f.read()

decrypted = key.decrypt(data)


with open (file, 'wb') as f:
    f.write(decrypted)