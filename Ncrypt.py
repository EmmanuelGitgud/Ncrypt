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

    #splits file name into 2 parts
    #(filename,file extension)
    split_name = filename.split('.')
    file_n = split_name[0]
    file_x = split_name[-1]

    #checks if file is already encrypted before encrypting it
    if file_x != 'crypt':
        #open file
        with open(directory + filename, 'rb') as f:
            filename = f.read()

        #encrypt each file each loop passes
        token = key.encrypt(filename)

        #write each encrypted file back
        with open(os.path.join(directory , file_n +'.'+ file_x +'.crypt'), 'wb') as f:
            f.write(token)

        #remove the duplicate file after encrypting it
        os.remove(directory + filestring)



