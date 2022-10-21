# Emmanuel Arabit
# OCT 11 2022

import os
from tkinter import filedialog 
from cryptography.fernet import Fernet

def check_key(path):
    # import key
    try:
        with open(path + 'N.key','rb') as f:
            f.read()
            return True
    except:
        return False

def encrypt_dir(directory, key):
    """function that encrypts directory"""
    with open(key + 'N.key','rb') as f:
        key = f.read()
    key = Fernet(key)
        
    for filename in os.listdir(directory):
        str_fn = str(filename)
        temp = filename.split('.')
        file_name = temp[0]
        file_type = temp[-1]

        if file_type != 'crypt':
            #open file
            with open(directory + filename, 'rb') as f:
                filename = f.read()

            # encrypt each file each loop passes
            token = key.encrypt(filename)

            # write each encrypted file back
            with open(directory + str_fn, 'wb') as f:
                f.write(token)

            new_name = str(file_name +'.'+file_type + ".crypt")
            os.rename(directory + str_fn, directory + new_name)

def decrypt_dir(directory, key):
    with open(key + 'N.key','rb') as f:
        key = f.read()
    key = Fernet(key)

    # iterate through directory
    for filename in os.listdir(directory):
        str_fn = str(filename)
        temp = filename.split('.')
        file_name = temp[0]
        file_extension = temp[-2]
        file_dummyX = temp[-1]

        if file_dummyX == 'crypt':
            #open the file 
            with open(directory + filename, 'rb') as f:
                filename = f.read()

            #decrypts the file
            token = key.decrypt(filename)

            #write the file
            with open(directory + str_fn,'wb') as f:
                f.write(token)

            new_name = str(file_name+'.'+file_extension)
            os.rename(directory + str_fn, directory + new_name)
       
def select_dir():
    """function for selecting file path"""
    filepath = filedialog.askdirectory()
    return filepath