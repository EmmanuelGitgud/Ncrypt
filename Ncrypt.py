# Emmanuel Arabit
# OCT 11 2022

import os
from tkinter import filedialog 
from cryptography.fernet import Fernet

def check_key():
    # import key
    try:
        with open('N.key','rb') as f:
                key = f.read()
        key = Fernet(key)
        return key
    except:
        return False

def encrypt_dir(directory):
    """function that encrypts directory"""
    if check_key() is not False:
        key = check_key()
        # iterate through files inside directory
        for filename in os.listdir(directory):
            filestring = filename

            # splits file name into 2 parts
            # (filename,file extension)
            split_name = filename.split('.')
            file_n = split_name[0]
            file_x = split_name[-1]

            with open(directory + filename, 'rb') as f:
                    filename = f.read()

            # encrypt each file each loop passes
            token = key.encrypt(filename)

            # write each encrypted file back
            with open(os.path.join(directory , file_n +'.'+ file_x), 'wb') as f:
                f.write(token)

            # remove the duplicate file after encrypting it
            os.remove(directory + filestring)

def decrypt_dir(directory):
    if check_key() is not False:
        key = check_key()
        # iterate through directory
        for filename in os.listdir(directory):
            filestring = filename

            # splits file name into 3 parts
            # (filename, original file extension, .crypt)
            split_name = filename.split('.')
            file_n = split_name[0]
            file_x = split_name[-2]
            file_c = split_name[-1]

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

def select_dir():
    """function for selecting file path"""
    filepath = filedialog.askdirectory()
    return filepath