#Emmanuel Arabit
#OCT 11 2022
import os 
from cryptography.fernet import Fernet

#import key
with open('key.json','rb') as f:
    key = f.read()
key = Fernet(key)

#directory
directory = 'topsecret/'

#iterate through files inside directory
for filename in os.listdir(directory):
    filestring = filename

    #file name
    file_n = filename.split('.')
    file_n = file_n[0]

        #file extension
    file_x = filename.split('.')
    file_x = file_x[-1]

    if file_x != 'crypt':
        #open file
        with open(directory + filename, 'rb') as f:
            filename = f.read()

        #encrypt each file each loop passes
        token = key.encrypt(filename)

        #write each encrypted file back
        with open(os.path.join(directory , file_n +'.'+ file_x +'.crypt'), 'wb') as f:
            f.write(token)

        os.remove(directory + filestring)

        





