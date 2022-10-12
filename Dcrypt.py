import os
from cryptography.fernet import Fernet

#import key
with open('key.json','rb') as f:
    key = f.read()
key = Fernet(key)

#directory
directory = 'topsecret/'

#iterate through directory
for filename in os.listdir(directory):
    filestring = filename
    #crypt extension
    file_c = filename.split('.')
    file_c = file_c[-1]

    #checks if it is a crypt file before decrypting it
    if file_c == 'crypt':

        #file name
        file_n = filename.split('.')
        file_n = file_n[0]

        #file extension
        file_x = filename.split('.')
        file_x = file_x[-2]

        #open the file 
        with open(os.path.join(directory,filename), 'rb') as f:
            filename = f.read()

        #decrypts the file
        token = key.decrypt(filename)

        #write the file
        with open(os.path.join(directory, file_n +'.'+ file_x),'wb') as f:
            f.write(token)
        
        os.remove(directory + filestring)
        
        
