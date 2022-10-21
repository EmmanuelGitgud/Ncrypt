# Emmanuel Arabit
# OCT 11 2022

import os
from cryptography.fernet import Fernet

def check_key(path):
    """checks if key is in directory, returns false if it does not exist"""
    try:
        with open(path+'key.json','rb') as f:
            f.read()
            return True
    except:
        return False

def encrypt_dir(directory, key):
    """function that encrypts directory"""
    with open(key+'key.json','rb') as f:
        key = f.read()
    key = Fernet(key)
        
    for filename in os.listdir(directory):
        filestring = filename

        # splits file name into 2 parts
        # (filename,file extension)
        split_name = filename.split('.')
        file_n = split_name[0]
        file_x = split_name[-1]

        # checks if file is already encrypted before encrypting it
        if file_x != 'crypt':
            #open file
            with open(directory + filename, 'rb') as f:
                filename = f.read()

            # encrypt each file each loop passes
            token = key.encrypt(filename)

            # write each encrypted file back
            with open(os.path.join(directory , file_n +'.'+ file_x +'.crypt'), 'wb') as f:
                f.write(token)

            # remove the duplicate file after encrypting it
            os.remove(directory + filestring)

def decrypt_dir(directory, key):
    with open(key+'key.json','rb') as f:
        key = f.read()
    key = Fernet(key)

    # iterate through directory
    for filename in os.listdir(directory):
        filestring = filename

        # splits file name into 3 parts
        # (filename, original file extension, .crypt)
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

