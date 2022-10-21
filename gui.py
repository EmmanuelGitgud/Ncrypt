import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *
from Ncrypt import *

root = Tk()
root.title('Ncrypt')
root.resizable(False,False)

#functions
def select_dir():
    file_dir.delete(0,END)
    filepath = filedialog.askdirectory()
    file_dir.insert(0, filepath) 

def select_key():
    key_dir.delete(0,END)
    filepath = filedialog.askdirectory()
    key_dir.insert(0, filepath)

def encrypt_cliked():
    if check_key(key_dir.get()+'/') is not False:
        path = os.path.realpath(file_loc.get())
        os.startfile(path)
        encrypt_dir(file_loc.get()+'/', key_loc.get()+'/')
        messagebox.showinfo(title='encryption',message='encryption success you may close the window')
    else:
        messagebox.showerror('Error', 'Key not found in directory')
def decrypt_clicked():
    if check_key(key_dir.get()+'/') is not False:
        path = os.path.realpath(file_loc.get())
        os.startfile(path)
        decrypt_dir(file_loc.get()+'/', key_loc.get()+'/')
        messagebox.showinfo(title='decryption',message='decryption success you may close the window')
    else:
        messagebox.showerror('Error', 'Key not found in directory')
        
#font
current_font = ("Arial Bold", 15)

# declare
key_loc = tk.Variable()
file_loc = tk.Variable()

file_dir = Entry(root,width=70,textvariable=file_loc)
key_dir = Entry(root,width=70,textvariable=key_loc)

browse_key_button = Button(root,font=current_font, text='Browse key',command=select_dir())
browse_file_button = Button(root,font=current_font, text='Browse directory',command=select_dir())

main_label = Label(root,font=current_font, text='******************* Welcome To Ncrypt *******************\n\n- Browse for your key\n\n- Browse for the directory\n\n- Then encrypt / decrypt\n')

encrypt_button = Button(root,font=current_font, text='Encrypt Directory',height=2, width=4)
decrypt_button = Button(root,font=current_font, text='Decrypt Directory',height=2, width=4)

# grid
file_dir.grid(column=0, row=0, columnspan=2, sticky=(W), padx=10,pady=10)
key_dir.grid(column=0,row=1, columnspan=2, sticky=(W),padx=10,pady=10)

browse_file_button.grid(column=3, row=0, sticky=(E), padx=10,pady=10)
browse_key_button.grid(column=3, row=1, sticky=(E), padx=10,pady=10)

main_label.grid(column=0, row=2, columnspan=4, padx=10,pady=10)

encrypt_button.grid(column=0,columnspan=1 , row=3, sticky=(S,E,W), padx=10,pady=10)
decrypt_button.grid(column=1,columnspan=4 , row=3, sticky=(S,E,W), padx=10,pady=10)

# weights
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=3)

root.mainloop()