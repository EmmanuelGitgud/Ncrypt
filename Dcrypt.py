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

    #splits file name into 3 parts
    #(filename, original file extension, .crypt)
    split_name = filename.split('.')
    file_n = split_name[0]
    file_x = split_name[-2]
    file_c = split_name[-1]

    #checks if it is a crypt file before decrypting it
    if file_c == 'crypt':

        #open the file 
        with open(os.path.join(directory,filename), 'rb') as f:
            filename = f.read()

        #decrypts the file
        token = key.decrypt(filename)

        #write the file
        with open(os.path.join(directory, file_n +'.'+ file_x),'wb') as f:
            f.write(token)
        
        #remove the duplicate file after decrypting it
        os.remove(directory + filestring)
        
