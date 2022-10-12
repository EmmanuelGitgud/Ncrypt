#Emmanuel Arabit
#OCT 11 2022

import os 
from cryptography.fernet import Fernet

#import key
try:
    with open('key.json','rb') as f:
        key = f.read()
except:
    print('key not found\nmake sure key is in directory')
    exit()

key = Fernet(key)

def encrypt_dir(directory):
    """function that encrypts directory"""
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
            print(filestring + ' succesfully encrypted')
            os.remove(directory + filestring)           
    print('operation complete you may now close the window...')

def decrypt_dir(directory):
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
            print(filestring + ' succesfully decrypted')
            os.remove(directory + filestring)
    print('operation complete you may now close the window...')

print('********** Welcome to Ncrypt **********\n')

print('ENCRYPT - 1')
print('DECRYPT - 2\n')

user_in = input('please select 1 for encryption and 2 for decryption: ')
user_dir = input('please enter the file directory: \n')

if user_in == '1':
    encrypt_dir(user_dir + '\\')

elif user_in == '2':
    decrypt_dir(user_dir + '\\')

else:
    print('invalid input!')